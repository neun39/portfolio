from django.urls import path
from .views import UncompletedTaskListView,CompletedTaskListView

app_name = 'task'

urlpatterns = [
    path('uncompleted/', UncompletedTaskListView.as_view(), name='task_list_uncompleted'),
    path('completed/', CompletedTaskListView.as_view(), name='task_list_completed'),
]
