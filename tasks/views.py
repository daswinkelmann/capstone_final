from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskList(generic.ListView):
    model = Task
    # queryset = Task.objects.all()
    template_name = "tasks/index.html"
    context_object_name = "task_list"
    paginate_by = 4
    ordering = ['-created_at']


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
    else:    
        form = TaskForm()

    return render(request, "tasks/add_task.html", {"form": form})

