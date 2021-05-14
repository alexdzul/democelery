from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from .models import Subscriber, Post, Log


@shared_task
def notify_new_content_async(post_id):
    """
    Sending and email.
    :param post_id: A new post (content) in database.
    """
    post = Post.objects.get(id=post_id)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        html_content = f"¡Hola {subscriber.full_name}! Te informamos que tenemos " \
                       f"un nuevo contenido: <b>{post.title}<b>"
        msg = EmailMultiAlternatives(f"¡Nuevo contenido!", html_content, 'from@example.com', [subscriber.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        log = Log(sent_to=subscriber.email, data=html_content)
        log.save()



@shared_task
def notify_new_subscriber_async(subscriber_id):
    """
    Sending and email.
    :param staffs: A list of staff users objects.
    :param subscriber: A new subscriber in database.
    """
    subscriber = Subscriber.objects.get(id=subscriber_id)
    staffs = User.objects.filter(is_staff=True)
    for user in staffs:
        html_content = f"¡Hola {user.first_name}! Te informamos se "\
                       f"registró una nueva persona:" \
                       f"<p><b>Nombre:</b> {subscriber.full_name}<br> " \
                       f"<b>Email:</b> {subscriber.email}</p>"
        msg = EmailMultiAlternatives(f"¡Nuevo suscriptor!", html_content, 'from@example.com', [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        log = Log(sent_to=user.email, data=html_content)
        log.save()


@shared_task
def delete_log():
    logs = Log.objects.all()
    print(f"{logs.count()} logs identificados")
    if logs.count() > 0:
        logs.delete()
        print("Eliminamos log")
    else:
        print("Nada que eliminar")
