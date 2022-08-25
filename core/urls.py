from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url

from rest_framework import permissions, authentication
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


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
    path("content/" , include("content.urls")),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [url(r'^image/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})]