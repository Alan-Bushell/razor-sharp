# Generated by Django 3.2 on 2023-01-12 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='county',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='street_address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
