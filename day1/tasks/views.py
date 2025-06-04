from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from django.views import View 
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

class TaskToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.completed = not task.completed
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'task_list_uncompleted'))