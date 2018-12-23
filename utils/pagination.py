from collections import OrderedDict
from django.utils import six
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'page'  # default
    max_page_size = 100  # 最大页数


    """
    重写get_page_size，根据url中的page的值去判断是否进行分页
    if page = 0  不分页
    if page < 0 按照默认分页
    if page > 0 根据数值去查看具体页码内容
    """
    def get_page_size(self, request):
        if self.page_size_query_param:
            if self.max_page_size:
                page_size = min(int(request.query_params.get(self.page_query_param, 1)),
                                self.max_page_size)
                if page_size > 0:
                    return self.page_size
                elif page_size == 0:
                    return None
                else:
                    pass

        return self.page_size



