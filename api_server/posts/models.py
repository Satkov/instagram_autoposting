from django.db import models


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
