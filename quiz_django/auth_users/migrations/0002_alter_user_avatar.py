# Generated by Django 3.2a1 on 2021-02-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
