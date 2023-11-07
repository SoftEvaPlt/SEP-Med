from django.db import models



class User(models.Model):
    user_id = models.IntegerField(primary_key=True, db_comment='用户ID')
    user_account = models.CharField(unique=True, max_length=30, db_comment='用户账号')
    user_password = models.CharField(max_length=30, db_comment='用户密码')
    user_name = models.CharField(unique=True, max_length=20, db_comment='用户账号')
    user_authority = models.IntegerField(db_comment='用户权限')
    user_email = models.CharField(max_length=30, blank=True, null=True, db_comment='用户邮箱')
    user_phone = models.IntegerField(blank=True, null=True, db_comment='用户电话号码')

    class Meta:
        managed = True
        db_table = 'user'