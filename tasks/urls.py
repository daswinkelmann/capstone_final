from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('add/', views.add_task, name='add_task'),
    path('done/<int:pk>/', views.task_done, name='task_done'),
    path('<int:pk>/edit', views.edit_task, name='edit_task'),
    path('<int:pk>/delete', views.delete_task, name='delete_task'),
]
