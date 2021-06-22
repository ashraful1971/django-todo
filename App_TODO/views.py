from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from App_TODO.models import Todo

# Create your views here.

def index(request):
    data = Todo.objects.all().order_by('-id')
    return render(request, 'App_TODO/index.html', context={'todos':data})

def addItem(request):
    if request.method == 'POST':
        obj = Todo(name=request.POST['name'])
        obj.save()
    return HttpResponseRedirect(reverse('App_TODO:index'))

def removeItem(request, pk):
    obj = Todo.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('App_TODO:index'))

def editItem(request, pk):
    itemData = Todo.objects.get(pk=pk)
    data = Todo.objects.all().order_by('-id')
    return render(request, 'App_TODO/index.html', context={'todos':data, 'itemData':itemData})

def updateItem(request):
    if request.method == 'POST':
        data = request.POST
        todo = Todo.objects.get(pk=data['id'])
        todo.name = data['name']
        todo.save()
    return HttpResponseRedirect(reverse('App_TODO:index'))
