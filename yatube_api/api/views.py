from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ParseError

from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)
from .permissions import AuthorOrReadOnly, ReadOnly
from posts.models import Post, Group, Follow, User


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        following = get_object_or_404(
            User, username=self.request.data.get('following')
        )
        if Follow.objects.filter(
            user=user,
            following=following
        ) or user == following:
            raise ParseError()
        serializer.save(user=user, following=following)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
