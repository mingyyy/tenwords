# Generated by Django 2.2.2 on 2019-07-18 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responder',
            name='user',
        ),
    ]