from student_app import views
from django.urls import path
app_name = 'student_app'

urlpatterns=[
    path('', views.StudentListView.as_view(),name='list'),
]