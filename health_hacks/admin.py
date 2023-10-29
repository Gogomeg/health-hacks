from django.contrib import admin
from .models import HealthHack


@admin.register(HealthHack)
class HealthhacksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'hack_type',
        'content',
        'image',
    )
    list_filter = ('hack_type',)
