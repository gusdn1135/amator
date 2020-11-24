# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=20)  # Field name made lowercase.

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
    cap_eamil = models.CharField(max_length=45)
    cap_pnumber = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'team_acc'
        unique_together = (('id', 'team_name'),)
