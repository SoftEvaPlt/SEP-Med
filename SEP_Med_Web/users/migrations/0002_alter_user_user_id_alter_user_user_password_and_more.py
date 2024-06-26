# Generated by Django 4.2.4 on 2023-11-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.BigAutoField(
                db_comment="用户ID", primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_password",
            field=models.CharField(db_comment="用户密码", max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_phone",
            field=models.CharField(
                blank=True, db_comment="用户电话", default="", max_length=11, null=True
            ),
        ),
    ]
