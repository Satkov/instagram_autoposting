from django.contrib import admin

from .models import PhotoPost, VideoPost


class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'caption', 'img_url', 'location_id',
                    'user_tags', 'token', 'date_pub')
    search_fields = ("user_id",)
    list_filter = ("date_pub",)


class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'caption', 'vid_url', 'location_id',
                    'thump_offset', 'token', 'date_pub')
    search_fields = ("user_id",)
    list_filter = ("date_pub",)


admin.site.register(PhotoPost, PhotoPostAdmin)
admin.site.register(VideoPost, VideoPostAdmin)