# Generated by Django 4.2.7 on 2023-11-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_phone",
            field=models.CharField(
                blank=True, db_comment="用户电话号码", max_length=11, null=True
            ),
        ),
    ]
