# Generated by Django 3.0.3 on 2020-05-30 07:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('registration_time', models.DateTimeField(auto_now_add=True, verbose_name='Time Registered')),
                ('team_members_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), null=True, size=10)),
                ('team_members_age', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), null=True, size=10)),
                ('team_size', models.PositiveIntegerField(default=1)),
                ('event_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Event', verbose_name='Event Id')),
                ('user_Id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.User', verbose_name='UserID')),
            ],
        ),
    ]