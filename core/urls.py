from django.contrib import admin
from django.urls import path,include


from rest_framework import permissions, authentication
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Bolt APIs",
      default_version='v1',
      contact=openapi.Contact(email="akash.joshi@sayf.in"),
   ),
    public=False,
    permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser),
    authentication_classes=(authentication.TokenAuthentication, authentication.SessionAuthentication)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/" , include("users.urls")),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
