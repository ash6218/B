from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

#def say_hello(request):
#    return render(request, 'home.html', {'name1': 'Ashkan', 'name2':'Zahra'})

def home(request):
    form1 = Todo.objects.all()
    return render(request, 'home.html', {'form1':form1})

def detail(request, todo_id):
    form2 = Todo.objects.get(id= todo_id)
    return render(request, 'detail.html', {'form2':form2})

def delete(request, todo_id):
    Todo.objects.get(id= todo_id).delete()
    return redirect('home')