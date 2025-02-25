

from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method=='POST':

        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = forms.TaskForm()


    return render(request, 'add_task.html', {'form' : task_form})
def Edit(request,id):
    task=models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method=='POST':

        task_form = forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    


    return render(request, 'add_task.html', {'form' : task_form})


def Delete(request,id):
    task=models.Task.objects.get(pk=id)
    task.delete()
    return redirect('home')
