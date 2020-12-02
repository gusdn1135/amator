# Generated by Django 3.1.3 on 2020-12-02 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=10, primary_key=True, serialize=False)),
                ('pw', models.CharField(db_column='PW', max_length=20)),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('leaguecode', models.AutoField(db_column='LeagueCode', primary_key=True, serialize=False)),
                ('league_name', models.CharField(max_length=45)),
                ('league_date', models.DateField()),
                ('league_location', models.CharField(max_length=45)),
                ('participants', models.JSONField(blank=True, null=True)),
                ('waiting', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'league',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamcode', models.AutoField(db_column='TeamCode', primary_key=True, serialize=False)),
                ('participants', models.JSONField(blank=True, null=True)),
                ('waiting', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminAcc',
            fields=[
                ('id', models.OneToOneField(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='page.account')),
            ],
            options={
                'db_table': 'admin_acc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndivAcc',
            fields=[
                ('id', models.OneToOneField(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='page.account')),
                ('indiv_studentid', models.IntegerField(db_column='indiv_studentID')),
                ('indiv_name', models.CharField(max_length=5)),
                ('indiv_sex', models.CharField(max_length=2)),
                ('indiv_bdate', models.DateField()),
                ('indiv_belong', models.CharField(max_length=45)),
                ('indiv_address', models.CharField(max_length=45)),
                ('indiv_pnumber', models.CharField(max_length=11)),
                ('indiv_email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'indiv_acc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrgAcc',
            fields=[
                ('id', models.OneToOneField(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='page.account')),
                ('org_name', models.CharField(max_length=45)),
                ('org_belong', models.CharField(max_length=45)),
                ('cap_name', models.CharField(max_length=5)),
                ('cap_eamil', models.CharField(max_length=45)),
                ('cap_pnumber', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'org_acc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeamAcc',
            fields=[
                ('id', models.OneToOneField(db_column='ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='page.account')),
                ('team_name', models.CharField(max_length=45)),
                ('team_pic', models.TextField(blank=True, null=True)),
                ('team_belong', models.CharField(max_length=45)),
                ('cap_name', models.CharField(max_length=5)),
                ('cap_eamil', models.CharField(max_length=45)),
                ('cap_pnumber', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'team_acc',
                'managed': False,
            },
        ),
    ]
