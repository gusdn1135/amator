
from django.db import models


class Account(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=20)  # Field name made lowercase.

    # Account 객체 생성
    def create(self, id, pw):
        self.id = id
        self.pw = pw
        self.save()


    class Meta:
        managed = False
        db_table = 'account'


class AdminAcc(models.Model):
    id = models.OneToOneField(Account, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_acc'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IndivAcc(models.Model):
    id = models.OneToOneField(Account, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    indiv_studentid = models.IntegerField(db_column='indiv_studentID')  # Field name made lowercase.
    indiv_name = models.CharField(max_length=5)
    indiv_sex = models.CharField(max_length=2)
    indiv_bdate = models.DateField()
    indiv_belong = models.CharField(max_length=45)
    indiv_address = models.CharField(max_length=45)
    indiv_pnumber = models.CharField(max_length=11)
    indiv_email = models.CharField(max_length=45)
    teamcode = models.ForeignKey('Team', models.DO_NOTHING, db_column='TeamCode', blank=True, null=True)  # Field name made lowercase.

    # IndivAcc 객체 생성
    def create(self, id, indiv_name, indiv_studentid, indiv_belong, indiv_sex,
    indiv_bdate, indiv_address, indiv_pnumber, indiv_email):
        self.id = id
        self.indiv_name = indiv_name
        self.indiv_studentid = indiv_studentid
        self.indiv_belong = indiv_belong
        self.indiv_sex = indiv_sex
        self.indiv_bdate = indiv_bdate
        self.indiv_address = indiv_address
        self.indiv_pnumber = indiv_pnumber
        self.indiv_email = indiv_email
        self.save()

    class Meta:
        managed = False
        db_table = 'indiv_acc'
        unique_together = (('id', 'indiv_studentid'),)


class League(models.Model):
    leaguecode = models.AutoField(db_column='LeagueCode', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey('OrgAcc', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    league_name = models.CharField(max_length=45)
    league_date = models.DateField()
    league_location = models.CharField(max_length=45)
    participants = models.JSONField(blank=True, null=True)
    waiting = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'league'
        unique_together = (('leaguecode', 'id'),)


class OrgAcc(models.Model):
    id = models.OneToOneField(Account, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    org_name = models.CharField(max_length=45)
    org_belong = models.CharField(max_length=45)
    cap_name = models.CharField(max_length=5)
    cap_eamil = models.CharField(max_length=45)
    cap_pnumber = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'org_acc'


class Team(models.Model):
    teamcode = models.AutoField(db_column='TeamCode', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey('TeamAcc', models.DO_NOTHING, db_column='ID')  # Field name made lowercase.
    participants = models.JSONField(blank=True, null=True)
    waiting = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
        unique_together = (('teamcode', 'id'),)


class TeamAcc(models.Model):
    id = models.OneToOneField(Account, models.DO_NOTHING, db_column='ID', primary_key=True)  # Field name made lowercase.
    team_name = models.CharField(max_length=45)
    team_pic = models.TextField(blank=True, null=True)
    team_belong = models.CharField(max_length=45)
    cap_name = models.CharField(max_length=5)
    # 여기 ...^^ email인데 eamil로 오타났는데... DB 수정하기가 귀찮아서 일단 eamil로 써주세요 호호
    cap_eamil = models.CharField(max_length=45)
    cap_pnumber = models.CharField(max_length=11)

    # TeamAcc 객체 생성
    # 팀 사진은 문제가 많아서 일단 생성에서는 제외함
    def create(self, id, team_name, team_belong, cap_name, cap_eamil, cap_pnumber):
        self.id = id
        self.team_name = team_name
        self.team_belong = team_belong
        self.cap_name = cap_name
        self.cap_eamil = cap_eamil
        self.cap_pnumber = cap_pnumber
        self.save()

    class Meta:
        managed = False
        db_table = 'team_acc'
        unique_together = (('id', 'team_name'),)

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
