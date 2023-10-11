from celery import shared_task
from django.template.loader import get_template
from django.conf import settings, datetime
from django.contrib.sites.models import Site
from django.utils.html import escape
from .models import Post


@shared_task
def notify_posts(post_id):
    post = Post.objects.get(id=post_id)
    subject = f'Новая статья на сайте: {post.head}'
    message = get_template('account/email/email_send.html').render(Context({'post': post}))
    from_email = settings.DEFAULT_FROM_EMAIL
    to_emails = get_emails_from_users()
    send_mail(subject, message, from_email, [email + Site.objects.first().domain for email in to_emails], fail_silently=False)


