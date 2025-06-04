from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import Task
from .forms import TaskFrom
# Create your views here.

class UncompletedTaskListView(ListView):
    model = Task
    template_name = 'tasks/uncompleted_task_list.html' 
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(completed=False).order_by("-created_at")
    

class CompletedTaskListView(ListView):
    model = Task
    template_name = 'tasks/completed_task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(completed=True).order_by("-created_at")

class TaskCreateFormView(FormView):
    template_name  = "tasks/task_create.html"
    form_class = TaskFrom
    