from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle_completed/<int:task_id>/', views.toggle_completed, name='toggle_completed'),
]
