"""moviebase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
# from rest_framework_swagger.views import get_swagger_view
#
# schema_view = get_swagger_view(title='Pastebin API')
from rest_framework import routers
from authentication.views import UserViewSet
from attendence.views import AttendenceViewSet, StudentViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'attendences', AttendenceViewSet)

urlpatterns = [
    #url(r'^$', SwaggerUIView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^grappelli/', include('grappelli.urls')),

    #url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^docs/', include_docs_urls(title='My API title'))
    #
    #url(r'', include('rest_framework_swagger.urls')),
    url(r'^api/v1/', include(router.urls, namespace='web')),
    url(r'^api/v1/', include('authentication.urls', namespace='authentication')),

]
