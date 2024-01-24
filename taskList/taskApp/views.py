from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from datetime import datetime

from .models import Task


def index(request):
    allTasks = Task.objects.all()
    today = datetime.now()

    return render(request, 'taskApp/index.html', {
        "all_tasks": allTasks,
        "today": today,
    })


def todo_tasks(request):
    todoTasks = Task.objects.filter(isActive=True)
    return render(request, 'taskApp/todo_tasks.html', {
        "todo_tasks": todoTasks,
    })


def finished_tasks(request):
    finishedTasks = Task.objects.filter(isActive=False)
    displayedTasks = []

    for task in finishedTasks:
        if task.isDeleted == False:
            displayedTasks.append(task)

    return render(request, 'taskApp/finished_tasks.html', {
        "finished_tasks": displayedTasks,
    })


def create_task(request):
    if request.method == "GET":
        return render(request, 'taskApp/create_task.html')
    else:
        taskName = request.POST.get('task_name')
        taskDescription = request.POST.get('task_description')

        newTask = Task(name = taskName, description = taskDescription)
        newTask.save()
        return HttpResponseRedirect(reverse(index))
    

def finish_task(request, id):
    next_view = request.GET.get('next', 'index')
    
    finishedTask = Task.objects.get(pk=id)

    finishedTask.isActive = False
    finishedTask.save()

    if next_view == 'index':
        return HttpResponseRedirect(reverse(index))
    elif next_view == 'todo_tasks':
        return HttpResponseRedirect(reverse(todo_tasks))


def undo_task(request, id):
    task = Task.objects.get(pk=id)

    task.isActive = True
    task.save()
    return HttpResponseRedirect(reverse(finished_tasks))


def edit_task(request, id):
    editedTask = Task.objects.get(pk=id)
    id = editedTask.id
    taskName = editedTask.name
    taskDescription = editedTask.description
    taskDeadline = editedTask.deadline

    if request.method == "GET":
        return render(request, 'taskApp/edit_task.html', {
            "task_name": taskName,
            "task_description": taskDescription,
            "task_id": id,
            "task_deadline": taskDeadline,
        })
    else:
        if request.POST.get('task_name') == "":
            editedTask.name = taskName
        else:
            editedTask.name = request.POST.get('task_name')

        if request.POST.get('task_description') == "":
            editedTask.description = taskDescription
        else:
            editedTask.description = request.POST.get('task_description')

        if request.POST.get('task_deadline') == "":
            editedTask.deadline = taskDeadline
        else:
            editedTask.deadline = request.POST.get('task_deadline')
        editedTask.save()
        return HttpResponseRedirect(reverse(index))
    

def delete_task(request, id):
    if request.method == "POST":
        Task.objects.adelete(pk=id)

        # task = Task.objects.get(pk=id)

        # task.adelete()
        return HttpResponseRedirect(reverse(finished_tasks))
    else:
        return HttpResponseRedirect(reverse(finished_tasks))