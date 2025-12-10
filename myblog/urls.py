from django.contrib import admin
from django.urls import path, include # <--- Не забудьте додати include сюди!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')), # <--- Цей рядок підключає ваш новий файл
]