# Generated by Django 3.0.3 on 2020-05-30 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0032_auto_20200530_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='team_members_age',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='team_members_id',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='user_Id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='UserID'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
