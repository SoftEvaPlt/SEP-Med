from django.db import models

# Create your models here.
class SafetyIndicator(models.Model):
    si_id = models.IntegerField(primary_key=True, db_comment='安全指标ID')
    si_category = models.CharField(max_length=30, db_comment='指标分类')
    si_name = models.CharField(max_length=30, db_comment='安全指标名称')
    si_state = models.IntegerField(db_comment='安全指标状态')
    si_creator = models.CharField(max_length=30, db_comment='安全指标创建人')
    si_create_time = models.DateTimeField(db_comment='安全指标创建时间')

    class Meta:
        managed = True
        db_table = 'safety_indicator'


class Scene(models.Model):
    scene_id = models.IntegerField(primary_key=True, db_comment='场景ID')
    scene_name = models.CharField(max_length=30, db_comment='场景名称')
    scene_state = models.IntegerField(db_comment='场景状态')
    scene_description = models.CharField(max_length=200, db_comment='场景描述')
    scene_creator = models.CharField(max_length=30, db_comment='场景创建人')
    scene_create_time = models.DateTimeField(db_comment='场景创建时间')

    class Meta:
        managed = True
        db_table = 'scene'