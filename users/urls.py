from django.urls import path
from users import views

urlpatterns = [
    path("user-check" , views.user_check),
]
