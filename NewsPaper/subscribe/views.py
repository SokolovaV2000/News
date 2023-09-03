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
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        sub.save()
        html_content = render_to_string(
            'sub_created.html',
            {
                'subscribe': sub,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{sub.client_name} {sub.date.strftime("%Y-%M-%d")}',
            body=sub.message,  # это то же, что и message
            from_email='sokolovav2000@yandex.ru',
            to=['sokolovava2@mail.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()
        return redirect('/subscribe')