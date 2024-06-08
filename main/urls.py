from django.urls import path
from .views import index, send_email, blog

urlpatterns = [
    path('', index, name='index'),
    path('send_email/', send_email, name='send_email'),
    path('blog/', blog, name='blog'),
]

