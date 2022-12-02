from django.urls import path
from . import views


urlpatterns=[
    path('teachers_page/', views.teachers_page, name='teachers_page'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('delete_teacher/<int:pk>', views.delete_teacher, name='delete_teacher'),
    path('update_teacher/<int:pk>', views.update_teacher, name='update_teacher'),
    path('search_teacher/', views.search_teacher, name='search_teacher'),
]