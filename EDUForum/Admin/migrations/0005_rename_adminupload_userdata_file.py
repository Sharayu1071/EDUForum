# Generated by Django 4.0.3 on 2022-03-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_userdata_adminupload_userdata_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='adminupload',
            new_name='file',
        ),
    ]
