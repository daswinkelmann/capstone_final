from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Task
from .forms import TaskForm

# Create your views here.


class TaskList(generic.ListView):
    # model = Task
    # queryset = Task.objects.all()
    template_name = "tasks/index.html"
    context_object_name = "task_list"
    paginate_by = 4
    # ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        # If not logged in, show empty list
        if not user.is_authenticated:
            return Task.objects.none()
        # If logged-in: show their TODOs first, then DONEs
        todos = Task.objects.filter(user=user, status="TODO").order_by("-created_at")
        dones = Task.objects.filter(user=user, status="DONE").order_by("-created_at")
        return list(todos) + list(dones)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mode = self.request.GET.get("mode", "read")  # "read" or "manage"
        context["mode"] = mode
        return context


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


@login_required
def task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = "DONE"
    task.save()
    return redirect("home")


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            edited_task = form.save(commit=False)
            edited_task.user = request.user
            edited_task.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form": form})


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect("home")
