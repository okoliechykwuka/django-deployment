# Generated by Django 2.2.5 on 2019-11-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pics',
            new_name='profile_pic',
        ),
    ]
