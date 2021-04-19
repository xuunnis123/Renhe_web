"""Renhe_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from index_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',"index.html"),
    path('', views.IndexView.as_view()),
    path('case_app/',include('case_app.urls',namespace='case_app')),
    path('casememo_app/',include('casememo_app.urls',namespace='casememo_app')),
    path('file_app/',include('file_app.urls',namespace='file_app')),
    path('finance_app/',include('finance_app.urls',namespace='finance_app')),
    path('group_app/',include('group_app.urls',namespace='group_app')),
    path('member_app/',include('member_app.urls',namespace='member_app')),
    path('scholorship_app/',include('scholorship_app.urls',namespace='scholorship_app')),
    path('school_app/',include('school_app.urls',namespace='school_app')),
]