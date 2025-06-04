from django.urls import path
from .views import UncompletedTaskListView,CompletedTaskListView,TaskCreateView

app_name = 'tasks'

urlpatterns = [
    path('uncompleted/', UncompletedTaskListView.as_view(), name='task_list_uncompleted'),
    path('completed/', CompletedTaskListView.as_view(), name='task_list_completed'),
    path('create/',TaskCreateView.as_view(),name="task_create")
]
