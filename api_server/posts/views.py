from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PhotoPost, VideoPost
from .serializer import PostPhotoListSerializer, PostPhotoUpdateSerializer
from .serializer import VideoPostListSerializer


class APIPhotoPost(APIView):
    def get(self, request):
        """Возвращает список постов c фотографией, ожидающих публикации"""
        request_data = request.query_params
        counter = PhotoPost.objects.filter(user_id=request_data['user_id']).count()
        if counter > 1:
            photo_posts = PhotoPost.objects.all().filter(user_id=request_data['user_id']).order_by('date_pub')
            serializer = PostPhotoListSerializer(photo_posts, many=True)
        else:
            photo_posts = PhotoPost.objects.get(user_id=request_data['user_id'])
            serializer = PostPhotoListSerializer(photo_posts)
        return Response(serializer.data)

    def post(self, request):
        """Создаёт объект поста с фото"""
        request_data = request.query_params
        post = PhotoPost.objects.create(user_id=request_data['user_id'],
                                        caption=request_data['caption'],
                                        img_url=request_data['img_url'],
                                        location_id=request_data['location_id'],
                                        user_tags=request_data['user_tags'],
                                        date_pub=request_data['date_pub'],
                                        token=request_data['token'])
        serializer = PostPhotoListSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        """Редактирует значение одного из полей модели поста с фото"""
        request_data = request.query_params
        if new_field == 'token':
            post = PhotoPost.objects.get(user_id=request_data['user_id'])
            serializer = PostPhotoUpdateSerializer(post,
                                                   data={request_data['new_field']:
                                                         value},
                                                   partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        post = PhotoPost.objects.get(id=request_data['id'])
        value = request_data['value']
        if new_field == 'date_pub' or new_field == 'user_id':
            value = int(value)
        serializer = PostPhotoUpdateSerializer(post,
                                               data={request_data['new_field']:
                                                     value},
                                               partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request):
        '''Удаляет пост с фото'''
        request_data = request.query_params
        PhotoPost.objects.get(id=request_data['id']).delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class APIVideoPost(APIView):
    def get(self, request):
        """Возвращает список постов с видео польователя"""
        request_data = request.query_params
        counter = VideoPost.objects.filter(user_id=request_data['user_id']).count()
        if counter > 1:
            video_posts = VideoPost.objects.filter(user_id=request_data['user_id']).order_by('date_pub')
            serializer = VideoPostListSerializer(video_posts, many=True)
        else:
            video_posts = VideoPost.objects.get(user_id=request_data['user_id'])
            serializer = VideoPostListSerializer(video_posts)
        return Response(serializer.data)

    def post(self, request):
        """Создаёт объект поста с видео"""
        request_data = request.query_params
        post = VideoPost.objects.create(user_id=request_data['user_id'],
                                        caption=request_data['caption'],
                                        img_url=request_data['img_url'],
                                        location_id=request_data['location_id'],
                                        thump_offset=request_data['thump_offset'],
                                        date_pub=request_data['date_pub'],
                                        token=request_data['token'])
        serializer = VideoPostListSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        """Меняет одно из значений в модели поста с видео"""
        request_data = request.query_params
        post = VideoPost.objects.get(id=request_data['id'])
        value = request_data['value']
        if new_field == 'date_pub' or new_field == 'user_id':
            value = int(value)
        serializer = VideoPostListSerializer(post,
                                             data={request_data['new_field']:
                                                   value},
                                             partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request):
        """Удаляет пост с видео"""
        request_data = request.query_params
        VideoPost.objects.get(id=request_data['id']).delete()
        return Response(status=status.HTTP_202_ACCEPTED)
