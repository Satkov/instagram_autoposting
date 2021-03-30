from datetime import datetime

from django_q.tasks import schedule
from django_q.models import Schedule


def create_container_schedule(post_id, date_pub):
    """
    Добавляет задание на отправку контейнера с постом в Facebook
    """
    name = schedule(f'fb_api.facebook_api_operator.Container',
                    post_id=post_id,
                    schedule_type=Schedule.ONCE,
                    next_run=datetime.utcfromtimestamp(
                        date_pub).strftime('%Y-%m-%d %H:%M:%S')
                    )
    print(name.kwargs)
