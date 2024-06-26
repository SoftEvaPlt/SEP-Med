# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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


class SafetyIndicator(models.Model):
    si_id = models.IntegerField(primary_key=True, db_comment='安全指标ID')
    si_category = models.CharField(max_length=30, db_comment='指标分类')
    si_name = models.CharField(max_length=30, db_comment='安全指标名称')
    si_state = models.IntegerField(db_comment='安全指标状态')
    si_creator = models.CharField(max_length=30, db_comment='安全指标创建人')
    si_create_time = models.DateTimeField(db_comment='安全指标创建时间')

    class Meta:
        managed = False
        db_table = 'safety_indicator'


class Scene(models.Model):
    scene_id = models.IntegerField(primary_key=True, db_comment='场景ID')
    scene_name = models.CharField(max_length=30, db_comment='场景名称')
    scene_state = models.IntegerField(db_comment='场景状态')
    scene_description = models.CharField(max_length=200, db_comment='场景描述')
    scene_creator = models.CharField(max_length=30, db_comment='场景创建人')
    scene_create_time = models.DateTimeField(db_comment='场景创建时间')

    class Meta:
        managed = False
        db_table = 'scene'


class Task(models.Model):
    task_id = models.IntegerField(primary_key=True, db_comment='任务ID')
    task_name = models.CharField(unique=True, max_length=30, db_comment='任务名称')
    task_state = models.ForeignKey('TaskStateTable', models.DO_NOTHING, db_column='task_state', db_comment='任务状态')
    scene = models.ForeignKey(Scene, models.DO_NOTHING, db_comment='应用场景（场景ID）')
    task_creator = models.ForeignKey('User', models.DO_NOTHING, db_column='task_creator', db_comment='任务创建人（用户ID）')
    task_create_time = models.DateTimeField(db_comment='任务创建时间')
    product_name = models.CharField(unique=True, max_length=20, db_comment='产品名称')
    product_version = models.CharField(max_length=20, blank=True, null=True, db_comment='产品版本号')
    product_description = models.CharField(max_length=200, blank=True, null=True, db_comment='产品描述')
    product_td = models.TextField(db_column='product_TD', blank=True, null=True, db_comment='产品拓扑图')  # Field name made lowercase.
    product_ad = models.TextField(db_column='product_AD', blank=True, null=True, db_comment='产品架构图')  # Field name made lowercase.
    app_ip = models.PositiveIntegerField(db_column='app_IP', blank=True, null=True, db_comment='应用IP')  # Field name made lowercase.
    app_domain_name = models.CharField(max_length=200, blank=True, null=True, db_comment='应用域名')
    app_starting_url = models.CharField(db_column='app_starting_URL', max_length=200, blank=True, null=True, db_comment='起始URL')  # Field name made lowercase.
    app_port = models.IntegerField(blank=True, null=True, db_comment='应用端口')
    app_name = models.CharField(max_length=30, blank=True, null=True, db_comment='应用名称')
    app_os_version = models.CharField(max_length=30, blank=True, null=True, db_comment='操作系统版本')

    class Meta:
        managed = False
        db_table = 'task'


class TaskEvaluation(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True, db_comment='用户ID')  # The composite primary key (user_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, models.DO_NOTHING, db_comment='任务ID')
    task_evaluate_time = models.DateTimeField(db_comment='评审时间')

    class Meta:
        managed = False
        db_table = 'task_evaluation'
        unique_together = (('user', 'task'),)


class TaskOperation(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True, db_comment='用户ID')  # The composite primary key (user_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, models.DO_NOTHING, db_comment='任务ID')
    task_operate_time = models.DateTimeField(db_comment='最后操作时间')

    class Meta:
        managed = False
        db_table = 'task_operation'
        unique_together = (('user', 'task'),)


class TaskSi(models.Model):
    task = models.OneToOneField(Task, models.DO_NOTHING, primary_key=True, db_comment='任务ID')  # The composite primary key (task_id, si_id) found, that is not supported. The first column is selected.
    si = models.ForeignKey(SafetyIndicator, models.DO_NOTHING, db_comment='安全指标ID')

    class Meta:
        managed = False
        db_table = 'task_si'
        unique_together = (('task', 'si'),)


class TaskStateTable(models.Model):
    task_state_id = models.IntegerField(primary_key=True, db_comment='任务状态')
    task_state_name = models.CharField(max_length=30, db_comment='任务状态名称')

    class Meta:
        managed = False
        db_table = 'task_state_table'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, db_comment='用户ID')
    user_account = models.CharField(unique=True, max_length=30, db_comment='用户账号')
    user_password = models.CharField(max_length=30, db_comment='用户密码')
    user_name = models.CharField(unique=True, max_length=20, db_comment='用户账号')
    user_authority = models.IntegerField(db_comment='用户权限')
    user_email = models.CharField(max_length=30, blank=True, null=True, db_comment='用户邮箱')
    user_phone = models.CharField(max_length=11, blank=True, null=True, db_comment='用户电话号码')

    class Meta:
        managed = False
        db_table = 'user'
