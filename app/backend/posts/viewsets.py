from rest_framework import viewsets
from .serializers import PostSerializer
from .models import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()