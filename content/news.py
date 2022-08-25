from utils import responses

from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from rest_framework import views, response, status, permissions, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@swagger_auto_schema(
    method="GET",
    responses=responses.GET_RESPONSES,
    
)
@api_view(['GET'])
@permission_classes([])
def fetch_news(request):
    # Dummy data
    data = {
    "status": "ok",
    "totalResults": 2,
    "articles": [
    {
    "source": "The Star Online",
    "author": "Glenn CHAPMAN",
    "title": "Elon Musk lawyers seize on Twitter whistleblower revelations",
    "description": "Elon Musk’s lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billionaire’s buyout bid. Read full story",
    "url": "https://www.thestar.com.my/tech/tech-news/2022/08/25/elon-musk-lawyers-seize-on-twitter-whistleblower-revelations",
    "urlToImage": "https://apicms.thestar.com.my/uploads/images/2022/08/25/1710897.jpg",
    "publishedAt": "2022-08-25T04:35:00Z",
    "content": "SAN FRANCISCO: Elon Musks lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billi… [+2991 chars]"
    },
    {
    "source": "The Star Online",
    "author": "Glenn CHAPMAN",
    "title": "Elon Musk lawyers seize on Twitter whistleblower revelations",
    "description": "Elon Musk’s lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billionaire’s buyout bid. Read full story",
    "url": "https://www.thestar.com.my/tech/tech-news/2022/08/25/elon-musk-lawyers-seize-on-twitter-whistleblower-revelations",
    "urlToImage": "https://apicms.thestar.com.my/uploads/images/2022/08/25/1710897.jpg",
    "publishedAt": "2022-08-25T04:35:00Z",
    "content": "SAN FRANCISCO: Elon Musks lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billi… [+2991 chars]"
    },
    {
    "source": "The Star Online",
    "author": "Glenn CHAPMAN",
    "title": "Elon Musk lawyers seize on Twitter whistleblower revelations",
    "description": "Elon Musk’s lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billionaire’s buyout bid. Read full story",
    "url": "https://www.thestar.com.my/tech/tech-news/2022/08/25/elon-musk-lawyers-seize-on-twitter-whistleblower-revelations",
    "urlToImage": "https://apicms.thestar.com.my/uploads/images/2022/08/25/1710897.jpg",
    "publishedAt": "2022-08-25T04:35:00Z",
    "content": "SAN FRANCISCO: Elon Musks lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billi… [+2991 chars]"
    },
    {
    "source": "The Star Online",
    "author": "Glenn CHAPMAN",
    "title": "Elon Musk lawyers seize on Twitter whistleblower revelations",
    "description": "Elon Musk’s lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billionaire’s buyout bid. Read full story",
    "url": "https://www.thestar.com.my/tech/tech-news/2022/08/25/elon-musk-lawyers-seize-on-twitter-whistleblower-revelations",
    "urlToImage": "https://apicms.thestar.com.my/uploads/images/2022/08/25/1710897.jpg",
    "publishedAt": "2022-08-25T04:35:00Z",
    "content": "SAN FRANCISCO: Elon Musks lawyers jumped Aug 24 on the revelations of a Twitter whistleblower to try to force the platform to surrender vast amounts of information for their fight to cancel the billi… [+2991 chars]"
    }
    ]}
    return response.Response(data , status.HTTP_200_OK)