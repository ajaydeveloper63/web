# Generated by Django 4.2 on 2023-10-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_sign_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=55)),
                ('Email', models.EmailField(max_length=254)),
                ('Resume', models.ImageField(upload_to='uploads')),
                ('pic', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'jobtb',
            },
        ),
    ]
