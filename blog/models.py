from django.db import models
from django.utils import timezone

# 1. Додаємо кастомний менеджер (фільтрує тільки опубліковані пости)
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    # 2. Додаємо варіанти статусу (як перемикач)
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    
    # 3. Додаємо нове поле 'status' у базу
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                              choices=Status.choices, 
                              default=Status.DRAFT)

    # 4. Підключаємо менеджери
    objects = models.Manager() # Стандартний менеджер
    published = PublishedManager() # Наш новий менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title