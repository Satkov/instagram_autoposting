import time
from datetime import datetime

from django_q.tasks import schedule
from django_q.models import Schedule


def create_container_schedule(post_id, date_pub, content_type):
    """
    Добавляет задание на отправку контейнера с постом в Facebook
    """
    schedule_time = next_run_time(date_pub)
    if content_type == 'Photo':
        func_name = 'PhotoContainer'
    else:
        func_name = 'VideoContainer'

    schedule(f'fb_api.facebook_api_operator.{func_name}',
             post_id,
             schedule_type=Schedule.ONCE,
             next_run=datetime.utcfromtimestamp(
                 schedule_time).strftime('%Y-%m-%d %H:%M:%S')
             )


def publish_container_schedule(container_id, date_pub, user_id, token):
    schedule('fb_api.facebook_api_operator.ContainerPublisher',
             container_id,
             user_id,
             token,
             schedule_type=Schedule.ONCE,
             next_run=datetime.utcfromtimestamp(
                 date_pub).strftime('%Y-%m-%d %H:%M:%S')
             )


def next_run_time(date_pub):
    """
    Возвращает unix время за десять минут(или меньше)
    До нужного времени публикации
    """
    schedule_time = date_pub - 600
    if schedule_time > time.time():
        return schedule_time

    schedule_time = date_pub - ((time.time() - date_pub) / 2)
    return schedule_time
