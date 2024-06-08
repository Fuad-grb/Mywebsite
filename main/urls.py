from django.urls import path
from .views import index, send_email, blog
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('blog/', blog, name='blog'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
