from django.urls import path
from .views import NewsArticleList, NewsArticleDetail

urlpatterns = [
    path('news/', NewsArticleList.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsArticleDetail.as_view(), name='news-detail'),
]