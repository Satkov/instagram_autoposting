import requests
from posts.models import Post
from rest_framework.response import Response


def Container(post_id):
    """
    Создаёт контейнер с постом (Хранится 24 часа)
    """
    post = Post.objects.get(id=post_id)
    BASE_URL = f'https://graph.facebook.com/v8.0/{post.user_id}/media'
    params = {
        'caption': post.caption,
        'image_url': post.url,
        'location_id': post.location_id,
        'user_tags': post.user_tags,
        'access_token': post.token
    }

    if post.content_type == 'Video':
        params = {
            'media_type': 'VIDEO',
            'caption': post.caption,
            'video_url': post.url,
            'location_id': post.location_id,
            'thumb_offset': post.thumb_offset,
        }

    response = requests.post(BASE_URL,
                             params=params)

    try:
        container_id = response.json()['id']
    except KeyError:
        raise ValueError('Wrong user id')

    ContainerPublisher(container_id, post.user_id, post.token)


def ContainerPublisher(container_id, user_id, access_token):
    """
    Публикует контейнер с постом
    """
    params = {
        'access_token': access_token,
        'creation_id': container_id
    }
    requests.post(f'https://graph.facebook.com/v8.0/{user_id}/media_publish',
                  params=params)
