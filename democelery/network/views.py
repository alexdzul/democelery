from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Post, Subscriber
from django.contrib import messages


class Index(ListView):
    model = Post
    paginate_by = 100
    template_name = "index.html"


class CreateSubscriber(CreateView):
    model = Subscriber
    fields = "__all__"
    success_url = "/"
    template_name = "index.html"

    def get_success_url(self):
        messages.success(self.request, '<b>¡Yei!</b> Ahora recibirás por email todas '
                                       'las actualizaciones de nuestro contenido :D')
        return reverse('network:index')


