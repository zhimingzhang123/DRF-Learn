from django.shortcuts import render
from django.http import HttpResponse
from functools import partial
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
"""
# LOGIN_URL = 'https://www.baidu.com'
# login_required = partial(login_required, login_url=LOGIN_URL)
# 
# @login_required
# def index(request):
#     return HttpResponse('hello')

"""

from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.permissions import AllowAny
from .serializers import TagSerializer, ArticleListRetrieveSerializer, ArticleUpdateCreateSerializer,PersonSerializer, CitySerializer, CityLookSerializer
from rest_framework_bulk.generics import BulkModelViewSet
from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView, BulkDestroyAPIView

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ArticleUpdateCreateSerializer
    # 展示时候使用一个序列器，更新创建的时候使用另外一个序列器
    # def get_serializer_class(self):
    #     print(self.action)
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return ArticleListRetrieveSerializer
    #     else:
    #         return ArticleUpdateCreateSerializer


class TagView(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny, )


class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CityLookSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'name'

    # 批量添加，批量修改，批量删除
    # def allow_bulk_destroy(self, qs, filtered):
    #     return qs is filtered
    #
    # def bulk_destroy(self, request, *args, **kwargs):
    #     req_list = [ data['id'] for data in request.data ]
    #
    #
    #     qs = []
    #     for id in req_list:
    #         query = self.get_queryset().filter(id=id)
    #         qs.append(query)
    #
    #     filtered = self.filter_queryset(qs)
    #     if not self.allow_bulk_destroy(qs, filtered):
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #     self.perform_bulk_destroy(filtered)
    #
    #     return Response(status=status.HTTP_204_NO_CONTENT)


