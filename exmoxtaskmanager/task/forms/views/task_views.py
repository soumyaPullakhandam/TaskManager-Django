from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView

from task.models import Task
from task.forms.forms import TaskForm


def home_view(request):
    """
        View to get users list for forms
    """
    user_model = User.objects.filter(is_staff=False)
    return render(request, "home.html", {"user_model": user_model})


def task_list(request, pk):
    """
        View to get task list based on user list for forms
    """
    user_model = User.objects.filter(is_staff=False)
    task_model = Task.objects.filter(user=pk)
    user_detail = User.objects.get(pk=pk)

    query = request.GET.get('q')

    if query:
        task_model = task_model.filter(
            Q(title__icontains=query)
        )

    return render(request, 'home.html',
                  {"user_model": user_model, 'task_model': task_model, 'user_detail': user_detail})


class TaskCreate(CreateView):
    """
        View to create Task for Forms
    """
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    """
        View to update Task for Forms
    """
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('home_view')


class TaskDelete(DeleteView):
    """
        View to delete Task for Forms
    """
    model = Task
    form_class = TaskForm
    template_name = 'delete_task.html'
    success_url = reverse_lazy('home_view')
