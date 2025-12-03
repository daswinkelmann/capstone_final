from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
]
