# Generated by Django 2.1.7 on 2019-03-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20190321_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
