# Generated by Django 2.2 on 2022-10-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_messages', '0004_message_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
