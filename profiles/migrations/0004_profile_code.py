# Generated by Django 2.2 on 2022-10-13 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]