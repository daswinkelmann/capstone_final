from django.shortcuts import render
from django.views import generic
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskList(generic.ListView):
    # model = Task
    queryset = Task.objects.all()
    template_name = "tasks/index.html"
    context_object_name = "task_list"
    paginate_by = 6





def add_task(request):
    form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})

