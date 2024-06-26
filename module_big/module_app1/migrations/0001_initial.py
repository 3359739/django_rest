# Generated by Django 4.2 on 2024-05-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="house",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="房屋名称")),
                ("address", models.CharField(max_length=100, verbose_name="房屋地址")),
                ("phone", models.CharField(max_length=11, verbose_name="联系电话")),
            ],
            options={
                "db_table": "house",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="user",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="用户名")),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                ("token", models.CharField(max_length=100, verbose_name="token")),
            ],
            options={
                "db_table": "user",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="user1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="用户名")),
                ("password", models.CharField(max_length=100, verbose_name="密码")),
                ("token", models.CharField(max_length=100, verbose_name="token")),
            ],
            options={
                "db_table": "user1",
                "managed": True,
            },
        ),
    ]
