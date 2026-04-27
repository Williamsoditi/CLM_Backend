from django.urls import path
from .views import NewsArticleList, NewsArticleDetail, GalleryImageList

urlpatterns = [
    path('news/', NewsArticleList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsArticleDetail.as_view(), name='news-detail'),
    path('gallery/', GalleryImageList.as_view(), name='gallery-image-list'),
]