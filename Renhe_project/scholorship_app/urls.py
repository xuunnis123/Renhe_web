from scholorship_app import views
from django.urls import path
app_name = 'scholorship_app'
urlpatterns=[
    path('', views.ScholorshipListView.as_view(),name='list'),
    path('<int:pk>/', views.ScholorshipDetailView.as_view(), name='detail'),
    path('create/',views.ScholorshipCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ScholorshipUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ScholorshipDeleteView.as_view(), name='delete'),
]