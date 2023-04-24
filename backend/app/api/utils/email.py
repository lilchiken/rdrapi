from app.core.email import mail_service


def send_mail(mail: str):
    body = "Thanks for sub! See you later!"
    headers = "From: andryuhin2@yandex.ru\r\n"
    headers += f"To: {mail}\r\n" 
    headers += f"Subject: Thanks\r\n"
    email_message = headers + "\r\n" + body
    mail_service.sendmail(
        'andryuhin2@yandex.ru',
        mail,
        email_message
    )
