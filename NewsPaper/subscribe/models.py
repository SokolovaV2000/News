from django.db import models
from django.contrib.auth.models import User
from news.models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from datetime import datetime


class Subscribe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}: {self.category}'

    def subscribe(self, pk):
        name = self.name
        category = self.category
        category.subscribers.add()

        message = 'Вы подписались на рассылку новостей'
        return redirect('/subscribe')


