# Generated by Django 5.1.1 on 2024-09-30 08:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='comments',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
