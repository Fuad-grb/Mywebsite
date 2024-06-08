from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user_email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'New message from {name}'

        # Отправка сообщения администратору
        send_mail(
            subject,
            message,
            'fuad__1998@mail.ru',  # Ваш email от Mail.ru
            ['fuad__1998@mail.ru'],  # Список получателей (администратор)
            fail_silently=False,
        )

        # Отправка подтверждения пользователю
        confirmation_subject = 'Confirmation of Your Message'
        confirmation_message = f'Thank you for reaching out, {name}. We have received your message and will get back to you shortly.'

        send_mail(
            confirmation_subject,
            confirmation_message,
            'fuad__1998@mail.ru',  # Ваш email от Mail.ru
            [user_email],  # Email пользователя
            fail_silently=False,
        )

        return render(request, 'main/index.html', {'success': True})

    return HttpResponse('Invalid request method.')

def blog(request):
    return render(request, 'main/blog.html')