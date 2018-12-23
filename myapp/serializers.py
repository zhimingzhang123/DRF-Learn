from rest_framework import serializers
from collections import OrderedDict
from rest_framework_bulk.serializers import BulkListSerializer, BulkSerializerMixin
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


# 列表、详情
class ArticleListRetrieveSerializer(serializers.ModelSerializer):
    # ta = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ('id', 'url', 'name', 'ta')
        # depth = 2 # 不需要再定制嵌套序列化，默认会序列化展示所有字段


# 创建、更新
class ArticleUpdateCreateSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    # 主键序列化
    # ta = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    # 超链接展示
    # if many to many > 2 ,set many = True
    # ta = serializers.HyperlinkedIdentityField(view_name='article-detail',many=True)

    # 自定义展示
    ta = serializers.SerializerMethodField()

    def get_ta(self, obj):
        return [{
            "name": u.name
        } for u in obj.ta.all()]

    # 嵌套序列化
    # 更新、创建 都需要重写
    # ta = TagSerializer(many=True) # 如果存在manytomany更新，不应该设置read_only=True

    def create(self, validated_data):
        tags = validated_data.pop('ta')
        print(tags)
        print(validated_data)
        article = Article.objects.create(**validated_data)
        for tag in tags:
            t = tag.get('name')
            obj = Tag.objects.filter(name=t)[0]
            article.ta.add(obj)
        return article

    def update(self, instance, validated_data):
        print(validated_data)
        tags = validated_data.pop('ta')
        instance = super(ArticleUpdateCreateSerializer, self).update(instance, validated_data)
        instance.ta.clear()  # clear the m2m relation
        for tag in tags:
            t = tag.get('name')
            obj = Tag.objects.filter(name=t)[0]
            instance.ta.add(obj)

        return instance

    class Meta:
        model = Article
        fields = ('id', 'url', 'name', 'ta')
        # extra_kwargs = {
        #     'ta': {"read_only": True},
        # }


class CitySerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = City
        list_serializer_class = BulkListSerializer
        fields = ("id", "url", "name")


class CityLookSerializer(serializers.HyperlinkedModelSerializer):
    """自定义查找字段"""
    class Meta:
        model = City
        fields = ("id",'url', "name")
        extra_kwargs = {
            'url': {'view_name': 'city-detail', 'lookup_field': 'name'},
        }


class PersonSerializer(serializers.ModelSerializer):
    # ct = serializers.HyperlinkedRelatedField(view_name='city-detail', queryset=City.objects.all())

    class Meta:
        model = Person
        fields = ("id", "url", "name", "ct",)

    def to_representation(self, instance):
        self.fields['ct'] = serializers.HyperlinkedRelatedField(view_name='city-detail', read_only=True)
        return super(PersonSerializer, self).to_representation(instance)
