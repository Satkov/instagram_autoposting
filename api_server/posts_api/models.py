from datetime import datetime

from django.db import models
from django.db.models.signals import post_save, pre_delete
from .q_manager import create_container_schedule
from django.dispatch import receiver
from django_q.models import Schedule


class Post(models.Model):
    CHOICES = (
        ('Photo', 'Photo'),
        ('Video', 'Video'),
    )
    user_id = models.BigIntegerField(blank=False, null=False)
    caption = models.CharField(max_length=2200, blank=True, null=True)
    url = models.CharField(max_length=4000, blank=False, null=False)
    location_id = models.CharField(max_length=2000, blank=True, null=True)
    user_tags = models.CharField(max_length=2200, blank=True, null=True)
    thump_offset = models.CharField(max_length=2000, blank=True, null=True)
    token = models.CharField(max_length=2000, blank=False, null=False)
    date_pub = models.BigIntegerField(blank=False, null=False)
    content_type = models.CharField(max_length=200, blank=False,
                                    null=False, choices=CHOICES)
    schedule_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Post)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    При создании поста, содаётся задание на его публикацию
    При редактировании поста, редактируется время задания
    """
    if created:
        post = Post.objects.get(id=instance.id)
        create_container_schedule(instance.id, instance.date_pub, post)
    else:
        schedule = Schedule.objects.get(id=instance.schedule_id)
        schedule.next_run = datetime.utcfromtimestamp(
                             instance.date_pub).strftime('%Y-%m-%d %H:%M:%S')
        schedule.save()


@receiver(pre_delete, sender=Post)
def post_delete_receiver(sender, instance, *args, **kwargs):
    """
    При удалении поста, удаляется задание по его публикации
    """
    schedule = Schedule.objects.get(id=instance.schedule_id)
    schedule.delete()