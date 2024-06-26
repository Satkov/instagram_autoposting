# Generated by Django 2.2.6 on 2021-07-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('caption', models.CharField(blank=True, max_length=2200, null=True)),
                ('url', models.CharField(max_length=4000)),
                ('location_id', models.CharField(blank=True, max_length=2000, null=True)),
                ('user_tags', models.CharField(blank=True, max_length=2200, null=True)),
                ('thump_offset', models.CharField(blank=True, max_length=2000, null=True)),
                ('token', models.CharField(max_length=2000)),
                ('date_pub', models.BigIntegerField()),
                ('content_type', models.CharField(choices=[('Photo', 'Photo'), ('Video', 'Video')], max_length=200)),
                ('schedule_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
