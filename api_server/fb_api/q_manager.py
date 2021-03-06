import time
from datetime import datetime

from django_q.tasks import schedule
from django_q.models import Schedule


def create_container_schedule(post_id, user_id, caption, url, location_id, user_tags,
                              thump_offset, token, date_pub, content_type):
    """
    Добавляет задание на отправку контейнера с постом в Facebook
    """
    schedule_time = next_run_time(date_pub)
    schedule('fb_api.facebook_api_operator.',
             post_id,
             user_id,
             caption,
             url,
             location_id,
             user_tags,
             thump_offset,
             token,
             date_pub,
             content_type,
             schedule_type=Schedule.ONCE,
             next_run=datetime.utcfromtimestamp(schedule_time).strftime('%Y-%m-%d %H:%M:%S')
             )


def next_run_time(date_pub):
    """
    Возвращает время для планировки задачи
    """
    schedule_time = date_pub - 600
    if schedule_time > time.time():
        return schedule_time

    schedule_time = date_pub - ((time.time() - date_pub) / 2)
    return schedule_time
