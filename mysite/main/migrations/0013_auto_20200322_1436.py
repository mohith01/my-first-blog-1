# Generated by Django 3.0.3 on 2020-03-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200322_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='max_Team_size',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
