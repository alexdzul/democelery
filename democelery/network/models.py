from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Subscriber(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name=_("Email"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Suscriptor")
        verbose_name_plural = _("Suscriptores")


class Post(models.Model):
    title = models.CharField(verbose_name=_("Título"), max_length=500)
    content = models.TextField(verbose_name=_("Contenido"))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Creado por"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Publicación")
        verbose_name_plural = _("Publicaciones")


class Log(models.Model):
    sent_to = models.CharField(max_length=1000, verbose_name=_("Enviado a"))
    data = models.TextField(verbose_name=_("Data"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data

    class Meta:
        verbose_name = _("Log")
        verbose_name_plural = _("Logs")