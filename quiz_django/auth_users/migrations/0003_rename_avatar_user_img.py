# Generated by Django 3.2a1 on 2021-02-03 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='img',
        ),
    ]
