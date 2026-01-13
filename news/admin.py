from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'game', 'created_at']
    list_filter = ['game', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
