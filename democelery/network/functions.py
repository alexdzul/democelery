from django.core.mail import EmailMultiAlternatives


def notify_new_content(subscribers, post):
    """
    Sending and email.
    :param subscribers: A list of Subscriber objects.
    :param post: A new post (content) in database.
    """
    for subscriber in subscribers:
        html_content = f"¡Hola {subscriber.full_name}! Te informamos que tenemos " \
                       f"un nuevo contenido: <b>{post.title}<b>"
        msg = EmailMultiAlternatives(f"¡Nuevo contenido!", html_content, 'from@example.com', [subscriber.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


def notify_new_subscriber(staffs, subscriber):
    """
    Sending and email.
    :param staffs: A list of staff users objects.
    :param subscriber: A new subscriber in database.
    """
    for user in staffs:
        html_content = f"¡Hola {user.first_name}! Te informamos se "\
                       f"registró una nueva persona:" \
                       f"<p><b>Nombre:</b> {subscriber.full_name}<br> " \
                       f"<b>Email:</b> {subscriber.email}</p>"
        msg = EmailMultiAlternatives(f"¡Nuevo suscriptor!", html_content, 'from@example.com', [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
