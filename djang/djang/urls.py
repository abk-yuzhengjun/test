"""djang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from myapp import views
from djang import search, search2, testdb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('123/', views.index2),
    path('time/', views.current_datetime),
    re_path('hours_(\d{1,2})/', views.hours_ahead),
    path('', views.index),
    path('testdb/', testdb.testdb),
    path('testdb2/', testdb.testdb2),
    path('testdb3/', testdb.testdb3),
    path('testdb4/', testdb.testdb4),
    path('bookDb/', testdb.bookDb),
    path('search/', search.search),
    path('contact/', search.contact),
    path('search-post/', search2.search_post),
    path('test_form/', search.test_form),
]
