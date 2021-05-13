from django.urls import path
from . import views

app_name = 'network'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create-subscriber/', views.CreateSubscriber.as_view(), name='create-subscriber'),
]
