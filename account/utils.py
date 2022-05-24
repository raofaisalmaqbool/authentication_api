import email
from django.core.mail import EmailMessage
import os
# print('*********')
class Utill:
    print('*********   1')
    @staticmethod
    def send_email(data):
        print('*********   2')
        email = EmailMessage(
            subject=data['subject'],
            body= data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to = [data['to_email']]
        )
        print('*********   3')
        email.send()