from finance_app import views
from django.urls import path
app_name = 'finance_app'
urlpatterns=[
    path('', views.FinanceListView.as_view(),name='list'),
    path('<int:pk>/', views.FinanceDetailView.as_view(), name='detail'),
    path('create/',views.FinanceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.FinanceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.FinanceDeleteView.as_view(), name='delete'),
]