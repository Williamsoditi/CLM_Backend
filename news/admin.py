from django.contrib import admin
from .models import NewsArticle, GalleryImage

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ['published_date']
    date_hierarchy = 'published_date'
    
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'created_at')
    search_fields = ('caption',)
    list_filter = ['created_at']
    date_hierarchy = 'created_at'