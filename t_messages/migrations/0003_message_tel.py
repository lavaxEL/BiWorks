# Generated by Django 2.2 on 2022-10-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_messages', '0002_remove_message_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='tel',
            field=models.TextField(blank=True, null=True),
        ),
    ]