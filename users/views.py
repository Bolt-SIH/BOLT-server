
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from rest_framework import views, response, status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from users import models as users_models
from content import models as ContentModels


from utils import responses
# Create your views here.

#Check if users already exists
@swagger_auto_schema(
    method="POST",
    responses=responses.GET_RESPONSES,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='10 digits mobile number'),
        }
    )
)
@api_view(['POST'])
# @decorators.try_except
@permission_classes([])
@authentication_classes ([])
def user_check(request):
    email = request.data.get("email", None)
    data = {}
    data["status"] = False
    try:
        user = users_models.User.objects.get(email = email)
        if user:
            token = Token.objects.get(user=user)
            data["uuid"] = user.uuid
            data["token"] = str(token)
            data["status"] = True
        return response.Response(data, status.HTTP_200_OK)
    except:
        return response.Response(data, status.HTTP_200_OK)


@swagger_auto_schema(
    method="POST",
    responses=responses.GET_RESPONSES,
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, 
        properties={
            'age_bracket': openapi.Schema(type=openapi.TYPE_STRING, description='Add the age bracket'),
            'prefs': openapi.Schema(type= openapi.TYPE_ARRAY, items = openapi.TYPE_STRING, description='Add the user prefs'),
   
        }
    )
)
@api_view(['POST'])
# @decorators.try_except
@permission_classes([permissions.IsAuthenticated])
def userPrefs(request):
    age_bracket = request.data.get("age_bracket" , None)
    prefs = request.data.get("prefs" , None)
    user = users_models.User.objects.get(id = request.user.id)
    
    if(age_bracket):
        user.age_bracket = age_bracket
    
    if(prefs):
        for i in prefs:
            user.user_preference.add(ContentModels.Category.objects.get(Category = i))
    
    
    user.save()

    return response.Response({"status" : True} , status.HTTP_200_OK)