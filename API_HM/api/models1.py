# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#from pickle import FALSE
from django.db import models


class ApiUsert(models.Model):
    #id_user = models.AutoField(db_column='ID_User', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=30)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    passwordt = models.CharField(db_column='passwordT', max_length=225)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=20)  # Field name made lowercase.
    mail = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'api_usert'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Church(models.Model):
    #id_church = models.BigAutoField(db_column='ID_CHURCH', primary_key=True)  # Field name made lowercase.
    namet = models.CharField(db_column='nameT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    municipality = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    cp = models.IntegerField(blank=True, null=True)
    phone1 = models.IntegerField(blank=True, null=True)
    phone2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'church'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    #id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Parameter(models.Model):
    id_parameter = models.BigAutoField(db_column='ID_PARAMETER', primary_key=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='lastUpdate', blank=True, null=True)  # Field name made lowercase.
    waist = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    imc = models.IntegerField(blank=True, null=True)
    clock = models.IntegerField(blank=True, null=True)
    gds = models.IntegerField(blank=True, null=True)
    katz = models.IntegerField(blank=True, null=True)
    lwb = models.IntegerField(blank=True, null=True)
    sarcf = models.IntegerField(db_column='sarcF', blank=True, null=True)  # Field name made lowercase.
    pantcirs = models.IntegerField(db_column='pantCirs', blank=True, null=True)  # Field name made lowercase.
    leftstrong = models.IntegerField(db_column='leftStrong', blank=True, null=True)  # Field name made lowercase.
    rightstrong = models.IntegerField(db_column='rightStrong', blank=True, null=True)  # Field name made lowercase.
    higheststrong = models.IntegerField(db_column='highestStrong', blank=True, null=True)  # Field name made lowercase.
    sppbbalance = models.IntegerField(db_column='sppbBalance', blank=True, null=True)  # Field name made lowercase.
    standem = models.IntegerField(db_column='sTandem', blank=True, null=True)  # Field name made lowercase.
    tandem = models.IntegerField(blank=True, null=True)
    spds = models.IntegerField(db_column='spdS', blank=True, null=True)  # Field name made lowercase.
    mtss = models.IntegerField(db_column='mtsS', blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(blank=True, null=True)
    globalsppb = models.IntegerField(db_column='globalSppb', blank=True, null=True)  # Field name made lowercase.
    frailtysppb = models.IntegerField(db_column='frailtySppb', blank=True, null=True)  # Field name made lowercase.
    frailtycfs = models.IntegerField(db_column='frailtyCfs', blank=True, null=True)  # Field name made lowercase.
    gijon = models.IntegerField(blank=True, null=True)
    ospace = models.IntegerField(db_column='oSpace', blank=True, null=True)  # Field name made lowercase.
    otime = models.IntegerField(db_column='oTime', blank=True, null=True)  # Field name made lowercase.
    calculation = models.IntegerField(blank=True, null=True)
    memoryt = models.IntegerField(db_column='memoryT', blank=True, null=True)  # Field name made lowercase.
    eject = models.IntegerField(blank=True, null=True)
    totalmmse = models.IntegerField(db_column='totalMmse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'parameter'


class Usert(models.Model):
    #id_usert = models.BigAutoField(db_column='ID_USERT', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=10, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    passwordt = models.CharField(db_column='passwordT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usert'
