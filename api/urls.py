from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.getTask, name='tasks'),
    path('task-details/<int:pk>', views.getTaskDetail, name='task-details'),
    path('task-create/', views.CreateTask, name='task-create'),
    path('task-update/<int:pk>', views.UpdateTask, name='task-update'),
    path('task-delete/<int:pk>', views.DeleteTask, name='task-delete'),
]
