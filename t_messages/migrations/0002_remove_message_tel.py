# Generated by Django 2.2 on 2022-10-04 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t_messages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='tel',
        ),
    ]