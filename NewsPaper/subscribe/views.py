from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime

from .models import Subscribe


class SubscribeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_sub.html', {})

    def post(self, request, *args, **kwargs):
        sub = Subscribe(
            name=request.POST['name'],
            category=request.POST['category'],
        )
        sub.save()

        send_mail(
            subject=f'Новая подписка на рассылку от {sub.name}',
            message=f'Пользователь подписался на рассылку в категории {sub.category}',
            from_email='sokolovav2000@yandex.ru',
            recipient_list=['sokolovava2@mail.ru']
        )

        html_content = render_to_string(
            'sub_created.html',
            {
                'sub': sub,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{sub.name}',
            body=sub.category,
            from_email='sokolovav2000@yandex.ru',
            to=['sokolovava2@mail.ru'],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()

        mail_admins(
            subject=f'Новая подписка на категорию',
            message=f'Пользователь {sub.name} подписался на рассылку в категории {sub.category}',
        )

        return redirect('/subscribe')