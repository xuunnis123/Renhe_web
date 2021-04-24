from file_app import views
from django.urls import path
app_name = 'file_app'
urlpatterns=[
    path('', views.FileListView.as_view(),name='list'),
    path('<int:pk>/', views.FileDetailView.as_view(), name='detail'),
    path('create/',views.FileCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.FileUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.FileDeleteView.as_view(), name='delete'),
]