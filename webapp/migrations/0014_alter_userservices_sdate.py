# Generated by Django 4.2 on 2023-10-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_userservices_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservices',
            name='Sdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
