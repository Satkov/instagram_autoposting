# Generated by Django 2.2.6 on 2021-02-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210221_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='thump_offset',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
