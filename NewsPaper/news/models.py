from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    full_name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField('Категория', max_length=255, unique=True)

    def __str__(self):
        return self.name.title()


Article = 'AR'
News = "NW"
CHOICE = [
    (Article, 'Статья'),
    (News, 'Новость')
]


class Post(models.Model):
    type = models.CharField('Тип', max_length=2, choices=CHOICE, default=Article)
    head = models.CharField('Заголовок', max_length=255, unique=True)
    body = models.TextField('Текст')
    time_of = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    rating = models.IntegerField(default=0)
    related_name='posts'

    def get_context_data(self):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_absolute_url(self):
        return f'/post_detail/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')

    def __str__(self):
        return f'{self.head.title()}: {self.body[:124]}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.body[0:123]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.TextField('Текст')
    time_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()