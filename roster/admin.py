from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'jersey_number', 'position', 'height', 'weight')
    search_fields = ('name', 'jersey_number', 'position')
    list_filter = ('position',)
    ordering = ('jersey_number',)
    fieldsets = (
        (None, {
            'fields': ('name', 'jersey_number', 'position')
        }),
        ('Physical Attributes', {
            'fields': ('height', 'weight')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )