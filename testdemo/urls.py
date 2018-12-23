"""testdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from myapp.views import index

# from rest_framework.routers import DefaultRouter
from rest_framework_bulk.routes import BulkRouter
from myapp.views import ArticleView, TagView, PersonView, CityView

router = BulkRouter()
router.register('article', ArticleView, 'article')
router.register('tag', TagView, 'tag')
router.register('person', PersonView, 'person')
router.register('city', CityView, 'city')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    # url(r'^index/$', index,name='index'),
]
