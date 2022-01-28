from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, mixins

from posts.models import Post, Comment
from posts.permissions import IsAuthorOrReadOnly, IsAuthorOrAdminDeleteOrReadOnly
from posts.serializers import PostSerializer, CommentSerializer


# class PostApiList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#
# class DetailPost(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthorOrAdminDeleteOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class CommentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
class CommentViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# List (GET ALL)
# Retrieve (GET DETAIL)
# CREATE (POST)
# UPDATE/PARTIAL UPDATE (PUT/PATCH -> DETAILS)
# DESTROY (DELETE -> Details)
