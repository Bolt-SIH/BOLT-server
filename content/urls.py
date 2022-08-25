from django.urls import path
from content import articles

urlpatterns = [
    path("fetch-articles" , articles.fetch_articles),
]
