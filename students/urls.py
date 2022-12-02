from django.urls import path
from . import views

urlpatterns=[
    path('student_page/', views.student_page, name='student_page'),
    path('new_student/', views.new_student, name='new_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('search_student/', views.search_name, name='search_student'),
    
    
]