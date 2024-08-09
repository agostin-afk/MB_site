from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import routers
from posts.viewsets import PostViewSet
from usuarios.viewsets import CreateUserViewSet, LoginViewSet
from pagamentos.viewsets import PagamentosViewSet


route = routers.DefaultRouter()
route.register(r'posts', PostViewSet, basename='posts')
# route.register(r'perfil', PerfilViewSet)
route.register(r'createUser', CreateUserViewSet, basename='createUser')
route.register(r'loginUser', LoginViewSet, basename='loginUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('summernote/', include('django_summernote.urls')),
] + debug_toolbar_urls()
