from case_app import views
from django.urls import path
from django_filters.views import FilterView
from .filters import CaseFilter
app_name = 'case_app'
urlpatterns=[
    path('', FilterView.as_view(filterset_class=CaseFilter,template_name='case_app/case_list.html'),name='list'),
    path('<int:pk>/', views.CaseDetailView.as_view(), name='detail'),
    path('create/',views.case_register, name='create'),
    path('create/student',views.case_student, name='student'),
    path('create/finance',views.case_student_finance, name='finance'),
    path('create/case_save',views.case_save, name='save'),
    path('update/<int:pk>/', views.CaseUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CaseDeleteView.as_view(), name='delete'),
]