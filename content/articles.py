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
# @decorators.try_except
@permission_classes([])
def fetch_articles(request):
    # Dummy data
    Article_Model = models.Article.objects.all()
    article = []
    for i in Article_Model:
        article.append({
        "source": i.source,
        "author": i.source,
        "title": i.title,
        "description": i.description,
        "url": i.sourceURL,
        "urlToImage": request.build_absolute_uri(i.image.url),
        "publishedAt": None,
        "content": i.description
        },) 

    data = {
    "status": "ok",
        "totalResults": len(Article_Model),
        "articles": article}
        
    return response.Response(data , status.HTTP_200_OK)