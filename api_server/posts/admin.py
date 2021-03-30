from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'caption', 'url', 'location_id',
                    'user_tags', 'thump_offset', 'token', 'date_pub')
    list_filter = ("date_pub",)


admin.site.register(Post, PostAdmin)
