from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, PostForm
from .models import Post
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/blog.html', {'posts': posts})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    