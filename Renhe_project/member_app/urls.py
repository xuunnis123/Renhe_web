from member_app import views
from django.urls import path
app_name = 'member_app'
urlpatterns=[
    path('', views.MemberListView.as_view(),name='list'),
    path('<int:pk>/', views.MemberDetailView.as_view(), name='detail'),
    path('create/',views.MemberCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.MemberUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.MemberDeleteView.as_view(), name='delete'),
]