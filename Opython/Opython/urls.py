"""Opython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from Opythonapp.views import header_view,user_reg_view,login_view,signout_view
from serilaizerapp.views import userlist
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url('admin/', admin.site.urls),
    url('home/', header_view),
    url('user_registration/', user_reg_view),
    url('login/',login_view),
    url('signout/',signout_view),
    url('serialget/', userlist.as_view()),
    # path('serialget/(?P<pk>[0-9]+)', userlist.as_view ()),

]
