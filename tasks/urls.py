from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('add/', views.add_task, name='add_task'),
]
