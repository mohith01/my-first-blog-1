# Generated by Django 2.1.4 on 2020-03-15 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191013_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventseries',
            name='event_category',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_series',
        ),
        migrations.DeleteModel(
            name='EventSeries',
        ),
    ]
