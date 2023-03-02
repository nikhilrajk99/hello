from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Todo

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView


class TaskListView(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'task3'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvindex')


# Create your views here.
def index(request):
    task1 = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Todo(name=name,priority=priority,date=date)
        task.save()
        return redirect('/')
    return render(request, "index.html", {'task1': task1})


def delete(request, task_id):
    task2 = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        task2.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, id):
    task = Todo.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "edit.html", {'f': f, 'task': task})

