from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api_server.fb_api.q_manager import create_container_schedule


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


@receiver(post_save, sender=Post)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    Отправляет задание в Django-q при создании объекта поста
    """
    if created:
        create_container_schedule(instance.id,
                                  instance.user_id,
                                  instance.caption,
                                  instance.url,
                                  instance.location_id,
                                  instance.user_tags,
                                  instance.thump_offset,
                                  instance.token,
                                  instance.date_pub,
                                  instance.content_type
                                  )
