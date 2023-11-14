from django.shortcuts import render
from django import forms

tasks = ['foo', 'bar', 'baz']

class NewTasksForm(forms.Form):
    task = forms.CharField(label='New Task')

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks' : tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
    else:
        return render(request, 'tasks/add.html',{
            'form' : NewTasksForm()
        })
    return render(request, 'tasks/add.html', {
        'form': NewTasksForm()
    })
