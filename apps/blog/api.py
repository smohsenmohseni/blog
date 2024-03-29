# Third-party imports.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
)

from .models import Post, Comment, Category
from .permissions import HasAccessPermission
from .serializers import (
    PostModelSerializer,
    CommentModelSerializer,
    CategoryModelSerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [HasAccessPermission]

    @action(detail=True, methods=['GET'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.commetns.all()
        serializer = CommentModelSerializer(comments)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def make_publish(self, request, pk=None):
        post = self.get_object()
        post.draft = False
        post.save()
        serializer = self.get_serializer()
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def get_publish(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(draft=False)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [HasAccessPermission]
