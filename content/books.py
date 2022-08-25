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
# @decorators.try_except
@permission_classes([])
def fetch_books(request):
    # Dummy data
    data = [
    {
    "urlToImage": "https://m.media-amazon.com/images/I/31USneULtoL.jpg",
    "title": "The Almanack of Naval Ravikant",
    "author" : "Akash Joshi",
    "descritption": "Naval Ravikant is a successful entrepreneur from India who grew up in the United States. Naval managed to build wealth through investments and multiple streams of income, all while growing his spirituality to learn the secrets of a meaningful life."
    },
    {
    "urlToImage": "https://images-na.ssl-images-amazon.com/images/I/41RqKn3u-bL._SX324_BO1,204,203,200_.jpg",
    "title": "Mastermind: How to Think Like Sherlock Holmes",
    "author" : "Akash Joshi",
    "description": "Whether you’re passionate about crimes and the world of mystery or don’t have much to do with it, you’ve probably heard the names of Sherlock Holmes and Dr. Watson. The mystery-solving duo rose to fame by solving even the most difficult criminal cases in London, all through their astonishing brain power."
    },
    {
    "urlToImage": "https://m.media-amazon.com/images/I/81ZLwAwD-ML._AC_UY327_FMwebp_QL65_.jpg",
    "title": "Rich Dad Poor Dad",
    "author" : "Akash Joshi",
    "description": "Rich Dad Poor Dad is a modern classic of personal finance and our favorite finance book of all time. Although the book is controversial and often takes criticism, people still believe it’s worth reading. Otherwise, it wouldn’t have sold over 32 million copies."
    },
    {
    "urlToImage": "https://m.media-amazon.com/images/I/71doP+hSREL._AC_UY327_FMwebp_QL65_.jpg",
    "title": "Zero to One",
    "author" : "Akash Joshi",
    "description": "There are books that give you great strategies for selling, marketing and planning your business. And then there are books that tell you to forget about all of that, so you can take an approach that’s so radically different, that you won’t even play in the same league as the readers of those other books."
    },
    {
    "urlToImage": "https://m.media-amazon.com/images/I/81WX9cDLUZL._AC_UY327_FMwebp_QL65_.jpg",
    "title": "Essentialism",
    "author" : "Akash Joshi",
    "description": "Published in early 2014, Greg McKeown’s Essentialism is a million-copy bestseller on how to get more out of your life by doing less. Remember how Steve Jobs said focus was about saying no? This book is all about how you can take this concept and apply it to your whole life."
    },
    {
    "urlToImage": "https://m.media-amazon.com/images/I/71g2ednj0JL._AC_UY327_FMwebp_QL65_.jpg",
    "title": "The Psychology of Money",
    "author" : "Akash Joshi",
    "description": "Our personal finances play a huge role in our lives. And yet people rarely discuss them and educate themselves on this topic. For this reason, many presumptions and false ideas about money have emerged over the years. They think having money is a result of luck or that rich people are all inheritors. Or perhaps wealth belongs only to those who disrupt the world and benefit from their discoveries."
    }
    ]
    return response.Response(data , status.HTTP_200_OK)