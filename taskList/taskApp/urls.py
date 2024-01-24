from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_tasks', views.todo_tasks, name='todo_tasks'),
    path('finished_tasks', views.finished_tasks, name='finished_tasks'),
    path('create_task', views.create_task, name='create_task'),
    path('finish_task/<int:id>', views.finish_task, name='finish_task'),
    path('undo_task/<int:id>', views.undo_task, name='undo_task'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
]