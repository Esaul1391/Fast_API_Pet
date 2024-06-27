from app.tasks.celery_app import celery

@celery.tasks(name='periodic_tasks')
def pereodic_tasks():
    print("Задача по расписанию")