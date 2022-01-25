from django.shortcuts import render
from rest_framework import generics, permissions

from posts.models import Post
from posts.permissions import IsAuthorOrReadOnly, IsAuthorOrAdminDeleteOrReadOnly
from posts.serializers import PostSerializer


class PostApiList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrAdminDeleteOrReadOnly]
