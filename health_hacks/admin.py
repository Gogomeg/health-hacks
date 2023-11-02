from django.contrib import admin
from .models import HealthHack
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HealthHack)
class HealthhacksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'hack_type',
        'content',
        'image',
    )
    list_filter = ('hack_type',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
