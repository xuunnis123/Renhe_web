from case_app import views
from django.urls import path
app_name = 'case_app'
urlpatterns=[
    path('', views.CaseListView.as_view(),name='list'),
    path('<int:pk>/', views.CaseDetailView.as_view(), name='detail'),
    path('create/',views.CaseCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.CaseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CaseDeleteView.as_view(), name='delete'),
]