from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('add/', views.TaskCreate.as_view(), name='add_task')
]
