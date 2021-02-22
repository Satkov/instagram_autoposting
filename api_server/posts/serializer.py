from rest_framework import serializers

from .models import PhotoPost, VideoPost


class PostPhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_id', 'caption', 'img_url', 'location_id',
                  'user_tags', 'date_pub')
        model = PhotoPost


class PostPhotoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_id', 'caption', 'img_url', 'location_id',
                  'user_tags', 'token', 'date_pub')
        model = PhotoPost


class VideoPostListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user_id', 'caption', 'vid_url', 'location_id',
                  'thump_offset', 'thump_offset', 'date_pub')
        model = VideoPost
