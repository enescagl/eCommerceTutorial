# Generated by Django 2.0.3 on 2018-03-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='my location default', max_length=120, null=True),
        ),
    ]
