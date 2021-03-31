from datetime import datetime

from django_q.tasks import schedule
from django_q.models import Schedule


def create_container_schedule(post_id, date_pub, post):
    """
    Добавляет задание на отправку контейнера с постом в Facebook
    """
    scheduler = schedule(f'fb_api.facebook_api_operator.Container',
                         post_id=post_id,
                         schedule_type=Schedule.ONCE,
                         next_run=datetime.utcfromtimestamp(
                             date_pub).strftime('%Y-%m-%d %H:%M:%S')
                         )
    """
    Записывает в объект id задания, 
    которое для него запланировано
    """
    post.schedule_id = scheduler.id
    post.save()
