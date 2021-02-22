from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PhotoPost, VideoPost
from .serializer import PostPhotoListSerializer, PostPhotoUpdateSerializer
from .serializer import VideoPostListSerializer


class APIPhotoPost(APIView):
    def get(self, request, user_id):
        """Возвращает список постов c фотографией, ожидающих публикации"""
        photo_posts = PhotoPost.objects.filter(user_id=user_id).order_by('date_pub')
        counter = PhotoPost.objects.filter(user_id=user_id).count()
        if counter > 1:
            serializer = PostPhotoListSerializer(photo_posts, many=True)
        else:
            serializer = PostPhotoListSerializer(photo_posts)
        return Response(serializer.data)

    def post(self, request, user_id, caption, img_url,
             location_id, user_tags, date_pub, token):
        """Создаёт объект поста с фото"""
        post = PhotoPost.objects.create(user_id=user_id, caption=caption,
                                        img_url=img_url, location_id=location_id,
                                        user_tags=user_tags, date_pub=date_pub,
                                        token=token)
        serializer = PostPhotoListSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id, new_field, value):
        """Редактирует значение одного из полей модели поста с фото"""
        post = PhotoPost.objects.get(id=id)
        if new_field == 'date_pub' or new_field == 'user_id':
            value = int(value)
        serializer = PostPhotoUpdateSerializer(post, data={new_field: value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        '''Удаляет пост с фото'''
        PhotoPost.objects.get(id=id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class APIVideoPost(APIView):
    def get(self, request, user_id):
        """Возвращает список постов с видео польователя"""
        video_posts = VideoPost.objects.filter(user_id=user_id).order_by('date_pub')
        counter = VideoPost.objects.filter(user_id=user_id).count()
        if counter > 1:
            serializer = VideoPostListSerializer(video_posts, many=True)
        else:
            serializer = VideoPostListSerializer(video_posts)
        return Response(serializer.data)

    def post(self, request, user_id, caption, vid_url,
             location_id, thump_offset, token, date_pub):
        """Создаёт объект поста с видео"""
        post = VideoPost.objects.create(user_id=user_id, caption=caption,
                                        vid_url=vid_url, location_id=location_id,
                                        thump_offset=thump_offset, date_pub=date_pub,
                                        token=token)
        serializer = VideoPostListSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id, new_field, value):
        """Меняет одно из значений в модели поста с видео"""
        post = VideoPost.objects.get(id=id)
        if new_field == 'date_pub' or new_field == 'user_id':
            value = int(value)
        serializer = VideoPostListSerializer(post, data={new_field: value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        """Удаляет пост с видео"""
        VideoPost.objects.get(id=id).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
