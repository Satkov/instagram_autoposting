from django.db import models


class PhotoPost(models.Model):
    """Модель хранит объект поста, в котором используется фотография."""
    user_id = models.BigIntegerField(blank=False, null=False)
    caption = models.CharField(max_length=2200, blank=True, null=True)
    img_url = models.CharField(max_length=4000, blank=False, null=False)
    location_id = models.CharField(max_length=2000, blank=True, null=True)
    user_tags = models.CharField(max_length=2200, blank=True, null=True)
    token = models.CharField(max_length=2000, blank=False, null=False)
    date_pub = models.BigIntegerField(blank=False, null=False)


class VideoPost(models.Model):
    """Модель хранит объект поста, в котором используется видео."""
    user_id = models.BigIntegerField(blank=False, null=False)
    caption = models.CharField(max_length=2200, blank=True, null=True)
    vid_url = models.CharField(max_length=2000, blank=False, null=False)
    location_id = models.CharField(max_length=2000, blank=True, null=True)
    thump_offset = models.CharField(max_length=2000, blank=True, null=True)
    token = models.CharField(max_length=2000, blank=False, null=False)
    date_pub = models.BigIntegerField(blank=False, null=False)
