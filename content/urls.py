from django.urls import path
from content import articles , news , books

urlpatterns = [
    path("fetch-articles" , articles.fetch_articles),
    path("fetch-news" , news.fetch_news),
    path("fetch-books" , books.fetch_books),
]
