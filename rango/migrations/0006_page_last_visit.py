# Generated by Django 2.1.5 on 2020-03-14 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 14, 14, 55, 26, 899139, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
