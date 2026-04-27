from rest_framework import serializers
from .models import *

class NewsArticleSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    image_url = serializers.SerializerMethodField()                            
    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'slug', 'content', 'published_date', 'image_url']
        
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        
class GalleryImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = GalleryImage
        fields = ['id', 'caption', 'image_url', 'created_at']
        
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None