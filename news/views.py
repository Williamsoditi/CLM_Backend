from rest_framework import generics
from .models import NewsArticle 
from .serializers import NewsArticleSerializer

class NewsArticleList(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    # pagination_class = None  # Disable pagination if not needed

class NewsArticleDetail(generics.RetrieveAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    # pagination_class = None  # Disable pagination if not needed