"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from user.views import SignUp, UserDetail
from user.viewsadvertise import AdvertiseList
from user.views import Otp
#from user.views import showData

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),
  #  path('view/', showData(),name='show data')
    url(r'^api/show/$', SignUp.as_view(), name='user_list'),
    url(r'^api/showad/$',AdvertiseList.as_view(),name='show add'),
    url(r'^api/showad/(?P<id>\d+)/$',AdvertiseList.as_view(),name='delete ad'),
    url(r'^api/otp/(?P<userId>\d+)/$',Otp.as_view(),name = 'otp store')

]
