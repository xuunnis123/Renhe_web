
from school_app import views
from django.urls import path
from django_filters.views import FilterView
from .filters import SchoolFilter
app_name = 'school_app'

urlpatterns=[
    path('', FilterView.as_view(filterset_class=SchoolFilter,template_name='school_app/school_list.html'),name='list'),
    #path('',views.school2_filter, name='school_filter'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/',views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path('school/filter/', views.school_filter, name='school_search'),
]