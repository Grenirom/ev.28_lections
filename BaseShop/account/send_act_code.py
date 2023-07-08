from django.core.mail import send_mail

HOST = '127.0.0.1:8000'


def send_activation_email(user, code):
    link = f'http://{HOST}/account/activate/{code}'
    send_mail(
        'Подтверждение регистрации аккаунта',
        'Здравствуйте, для активации вашего аккаунта вам необходимо перейти по ссылке ниже:',
        
    )