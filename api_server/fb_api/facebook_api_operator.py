import requests
from posts.models import Post
from .q_manager import publish_container_schedule

def PhotoContainer(self, post_id):
    '''
    Создаёт контейнер с постом (Хранится 24 часа)
    '''
    post = Post.objects.get(id=post_id)
    BASE_URL = f'graph.facebook.com/{post.user_id}/media/'
    params = {
        'caption':post.caption,
        'image_url':post.url,
        'location_id':post.location_id,
        'user_tags':post.user_tags,
    }
    container_id = requests.post(BASE_URL,
                                 access_token=post.token,
                                 params=params)
    '''
    Создаёт задачу для публикации контейнера в нужное время
    '''
    publish_container_schedule(container_id['id'], post.date_pub,
                               post.user_id, post.token)


def VideoContainer(self, post_id):
    '''
    Создаёт контейнер с постом (Хранится 24 часа)
    '''
    post = Post.objects.get(id=post_id)
    BASE_URL = f'graph.facebook.com/{post.user_id}/media/'
    params = {
        'media_type': 'VIDEO',
        'caption':post.caption,
        'video_url':post.url,
        'location_id':post.location_id,
        'thumb_offset':post.thumb_offset,
    }
    container_id = requests.post(BASE_URL,
                                 access_token=post.token,
                                 params=params)
    '''
    Создаёт задачу для публикации контейнера в нужное время
    '''
    publish_container_schedule(container_id['id'], post.date_pub,
                               post.user_id, post.token)



def ContainerPublisher(container_id, user_id, access_token):
    '''
    Публикует контейнер с постом
    '''
    requests.post(f'graph.facebook.com/{user_id}/media/{container_id}/',
                  access_token=access_token)
