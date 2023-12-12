from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'


class TaskDetails(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('Name', 'Priority', 'Date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('Name', '')
        priority = request.POST.get('Priority', '')
        date = request.POST.get('Date', '')
        task = Task(Name=name, Priority=priority, Date=date)
        task.save()

    return render(request, "home.html", {'task': task1})

# def details(request):
#
#     return render(request, 'details.html')


def delete(request, taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task=Task.objects.get(id=id)
    f=Todoforms(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})
