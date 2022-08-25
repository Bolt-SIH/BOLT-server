from utils import responses

from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from rest_framework import views, response, status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from content import models

@swagger_auto_schema(
    method="GET",
    responses=responses.GET_RESPONSES,
    
)
@api_view(['GET'])
@permission_classes([])
def fetch_news(request):
    News = models.news.objects.all()
    article = []
    for i in News:
        article.append({
        "source": i.source,
        "author": i.source,
        "title": i.title,
        "description": i.description,
        "url": i.sourceURL,
        "urlToImage": request.build_absolute_uri(i.image.url).replace("images/images" , "images/"),
        "publishedAt": None,
        "content": i.description
        },) 

    data = {
    "status": "ok",
        "totalResults": len(News),
        "articles": article}
        
    return response.Response(data , status.HTTP_200_OK)