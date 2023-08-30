from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    full_name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField('Категория', max_length=255, unique=True)


Article = 'AR'
News = "NW"
CHOICE = [
    (Article, 'Статья'),
    (News, 'Новость')
]


class Post(models.Model):
    type = models.CharField('Тип', max_length=2, choices=CHOICE, default=Article)
    head = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Текст')
    time_of = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    rating = models.IntegerField(default=0)

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

