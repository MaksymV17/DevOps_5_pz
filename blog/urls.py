from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Головна сторінка блогу (список постів)
    path('', views.post_list, name='post_list'),
    # Сторінка конкретного поста (по ID)
    path('<int:id>/', views.post_detail, name='post_detail'),
]