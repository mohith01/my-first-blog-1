# Generated by Django 3.0.3 on 2020-05-29 22:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200530_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='team_members_age',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), null=True, size=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_members_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), null=True, size=10),
        ),
    ]
