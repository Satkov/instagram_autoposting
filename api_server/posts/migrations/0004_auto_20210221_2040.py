# Generated by Django 2.2.6 on 2021-02-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210221_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopost',
            name='vid_url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
