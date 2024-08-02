from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from posts.viewsets import PostViewSet
from usuarios.viewsets import PerfilViewSet, CreateUserViewSet

route = routers.DefaultRouter()
route.register(r'posts', PostViewSet)
route.register(r'perfil', PerfilViewSet)
route.register(r'createUser', CreateUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
]
