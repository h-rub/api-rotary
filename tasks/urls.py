from django.urls import path
from tasks.views import MyTasksList, TasksList, delete_task, CreateTask, TaskComplete
urlpatterns = [
    path('tasks/all', TasksList.as_view(), name="task_list"),
    path('task/delete/<int:id_task>', delete_task, name="delete_task"),

    path("task/create", CreateTask.as_view(), name="create_task"),

    path('tasks', MyTasksList.as_view(), name="my_Tasks"),
    path('task/update/<int:id_task>', TaskComplete.as_view(), name="complete_task")
]