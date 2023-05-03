from app.core.celery_app import celery_app
from app.api.utils import email as utils_emails
from app.core.redis import rediscli
from app.core.config import conf


email_set = conf.get('name_mails_set')


@celery_app.task
def send_email(email: str):
    if rediscli.sismember(email_set, email):
        raise ValueError('This email has been registered before')
    rediscli.sadd(email_set, email)
    utils_emails.send_mail(email)
