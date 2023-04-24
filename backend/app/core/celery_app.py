from celery import Celery

celery_app = Celery('worker', broker='redis://redis:6379/1')

celery_app.conf.task_routes = {
    'send_email': 'main-queue',
}
