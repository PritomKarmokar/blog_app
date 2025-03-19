from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdminManager(admin.ModelAdmin):
    list_display = [
        'title',
        'content',
    ]
    list_filter = [
        'created_at'
    ]

    ordering = ['created_at']