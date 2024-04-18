from django.db import models
from users.models import User
from administration.models import Scene,SafetyIndicator



class Task(models.Model):
    task_id = models.IntegerField(primary_key=True, db_comment='任务ID')
    task_name = models.CharField(unique=True, max_length=30, db_comment='任务名称')
    task_state = models.ForeignKey('TaskStateTable', models.DO_NOTHING, db_column='task_state', db_comment='任务状态')
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, db_comment='应用场景（场景ID）')
    task_creator = models.ForeignKey(User, on_delete=models.CASCADE, db_column='task_creator', db_comment='任务创建人（用户ID）')
    task_create_time = models.DateTimeField(db_comment='任务创建时间')
    product_name = models.CharField(unique=True, max_length=20, db_comment='产品名称')
    product_version = models.CharField(max_length=20, blank=True, null=True, db_comment='产品版本号')
    product_description = models.CharField(max_length=200, blank=True, null=True, db_comment='产品描述')
    product_td = models.ImageField(upload_to='images/', db_column='product_TD', blank=True, null=True, db_comment='产品拓扑图')  # Field name made lowercase.
    product_ad = models.ImageField(upload_to='images/', db_column='product_AD', blank=True, null=True, db_comment='产品架构图')  # Field name made lowercase.
    app_ip = models.PositiveIntegerField(db_column='app_IP', blank=True, null=True, db_comment='应用IP')  # Field name made lowercase.
    app_domain_name = models.CharField(max_length=200, blank=True, null=True, db_comment='应用域名')
    app_starting_url = models.CharField(db_column='app_starting_URL', max_length=200, blank=True, null=True, db_comment='起始URL')  # Field name made lowercase.
    app_port = models.IntegerField(blank=True, null=True, db_comment='应用端口')
    app_name = models.CharField(max_length=30, blank=True, null=True, db_comment='应用名称')
    app_os_version = models.CharField(max_length=30, blank=True, null=True, db_comment='操作系统版本')

    class Meta:
        managed = True
        db_table = 'task'

class TaskEvaluation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_comment='用户ID')  # The composite primary key (user_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, on_delete=models.CASCADE, db_comment='任务ID')
    task_evaluate_time = models.DateTimeField(db_comment='评审时间')

    class Meta:
        managed = True
        db_table = 'task_evaluation'
        unique_together = (('user', 'task'),)

class TaskOperation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_comment='用户ID')  # The composite primary key (user_id, task_id) found, that is not supported. The first column is selected.
    task = models.ForeignKey(Task, on_delete=models.CASCADE, db_comment='任务ID')
    task_operate_time = models.DateTimeField(db_comment='最后操作时间')

    class Meta:
        managed = True
        db_table = 'task_operation'
        unique_together = (('user', 'task'),)


class TaskSi(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, primary_key=True, db_comment='任务ID')  # The composite primary key (task_id, si_id) found, that is not supported. The first column is selected.
    si = models.ForeignKey(SafetyIndicator, on_delete=models.CASCADE, db_comment='安全指标ID')

    class Meta:
        managed = True
        db_table = 'task_si'
        unique_together = (('task', 'si'),)


class TaskStateTable(models.Model):
    task_state_id = models.IntegerField(primary_key=True, db_comment='任务状态')
    task_state_name = models.CharField(max_length=30, db_comment='任务状态名称')

    class Meta:
        managed = True
        db_table = 'task_state_table'


# class User(models.Model):
#     user_id = models.IntegerField(primary_key=True, db_comment='用户ID')
#     user_account = models.CharField(unique=True, max_length=30, db_comment='用户账号')
#     user_password = models.CharField(max_length=30, db_comment='用户密码')
#     user_name = models.CharField(unique=True, max_length=20, db_comment='用户账号')
#     user_authority = models.IntegerField(db_comment='用户权限')
#     user_email = models.CharField(max_length=30, blank=True, null=True, db_comment='用户邮箱')
#     user_phone = models.CharField(max_length=11, blank=True, null=True, db_comment='用户电话号码')

#     class Meta:
#         managed = True
#         db_table = 'user'
