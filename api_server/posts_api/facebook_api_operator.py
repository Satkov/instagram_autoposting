import requests

from .models import Post


def container(post_id):
    """
    Создаёт контейнер с постом (Хранится 24 часа)
    """
    post = Post.objects.get(id=post_id)
    base_url = f'https://graph.facebook.com/v8.0/{post.user_id}/media'
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

    response = requests.post(base_url,
                             params=params)

    try:
        container_id = response.json()['id']
    except KeyError:
        raise ValueError('Wrong user id')

    container_publisher(container_id, post.user_id, post.token)


def container_publisher(container_id, user_id, access_token):
    """
    Публикует контейнер с постом
    """
    params = {
        'access_token': access_token,
        'creation_id': container_id
    }
    requests.post(f'https://graph.facebook.com/v8.0/{user_id}/media_publish',
                  params=params)
