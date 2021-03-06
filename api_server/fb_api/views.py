from django_q.tasks import async_task, schedule
from django_q.models import Schedule
import time
from datetime import timedelta
from django.utils import timezone

def task_manager(post_id, content_type):
    schedule('db_api.testdef', post_id, content_type, schedule_type=Schedule.ONCE,
             next_run=timezone.now() + timedelta(seconds=10805))


def testdef(post_id, content_type):
    print('sajdahsd')
    print(post_id, content_type)
