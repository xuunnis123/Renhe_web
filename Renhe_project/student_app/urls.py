from student_app import views
from django.urls import path
app_name = 'student_app'

urlpatterns=[
    path('', views.StudentListView.as_view(),name='list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('create/',views.StudentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
    path('student/filter/', views.student_filter, name='student_search'),
]