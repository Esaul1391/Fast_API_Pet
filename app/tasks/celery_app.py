from celery import Celery
from celery.schedules import crontab


celery = Celery(
    'tasks',
    broker='redis://localhost:6379',
    include=['app.tasks.tasks', 'app.tasks.scheduled']
)

#   работа с расписание
celery.conf.beat_schedule = {
    'lubooe_nazvanie': {
        'task': 'periodic_tasks',
        'schedule': 10, #   запуск через определенное время
        # 'schedule': crontab(minute='30', hour='15'), #   более сложное расписание
    }
}
