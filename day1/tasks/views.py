from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.views import View 
from .models import Task
from .forms import TaskForm 
from django.urls import reverse_lazy
# Create your views here.

class UncompletedTaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list_uncompleted.html' 
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(completed=False).order_by("-created_at")
    

class CompletedTaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list_completed.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(completed=True).order_by("-created_at")

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_create.html" 
    success_url = reverse_lazy('task_list_uncompleted')
    

class TaskToggleCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.completed = not task.completed
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'task_list_uncompleted'))