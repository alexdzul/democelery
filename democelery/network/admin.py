from django.contrib import admin
from .models import Post, Subscriber


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_by", "timestamp")
    search_fields = ["title", "content", "created_by__first_name", "craeted_by__last_name",
                     "created_by__username", "created_by__email"]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "timestamp")
    search_fields = ["full_name", "email"]


