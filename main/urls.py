from django.urls import path
from .views import index, send_email, blog, register, create_post, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('blog/', blog, name='blog'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('create_post/', create_post, name='create_post'),
]
