import smtplib

from app.core.config import conf


mail_service = smtplib.SMTP(conf.get('smtp'), conf.get('smtp_port'))
mail_service.login(
    user=conf.get('mailserver'),
    password=conf.get('mailserver_pass')
)
mail_service.esmtp_features['auth'] = 'CRAM-MD5'
