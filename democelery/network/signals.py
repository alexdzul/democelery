from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Post, Subscriber
from .functions import notify_new_content, notify_new_subscriber


@receiver(post_save, sender=Post)
def send_mail_to_subscriber(sender, **kwargs):
    """
    Sending message to subscribers when exist a new post.
    When a post is created
    """
    if kwargs.get('created', False):
        post = kwargs.get("instance")
        notify_new_content(post.id)


@receiver(post_save, sender=Subscriber)
def new_subscriber(sender, **kwargs):
    """
    Sending message staff when exist a new subscriber.
    """
    if kwargs.get('created', False):
        subscriber = kwargs.get("instance")
        notify_new_subscriber(subscriber.id)
