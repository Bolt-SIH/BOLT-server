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
def fetch_books(request):
    # Dummy data
    Books_Model = models.books.objects.all()
    data = []
    for i in Books_Model:
        data.append(
            {
            "urlToImage": request.build_absolute_uri(i.image.url).replace("images/images" , "images/"),
            "title": i.title,
            "author" : i.author,
            "description": i.description
            },
        ) 


    return response.Response(data , status.HTTP_200_OK)