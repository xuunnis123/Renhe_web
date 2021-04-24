from index_app import views
from django.urls import path
app_name = 'index_app'

urlpatterns=[
    path('', views.IndexView.as_view(),name='index'),
]