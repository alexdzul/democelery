from django.core.mail import EmailMultiAlternatives
from .tasks import notify_new_content_async, notify_new_subscriber_async


def notify_new_content(post_id):
    """
    Sending and email.
    :param subscribers: A list of Subscriber objects.
    :param post: A new post (content) in database.
    """
    notify_new_content_async.delay(post_id)


def notify_new_subscriber(subscriber_id):
    """
    Sending and email.
    :param staffs: A list of staff users objects.
    :param subscriber: A new subscriber in database.
    """
    notify_new_subscriber_async.delay(subscriber_id)
