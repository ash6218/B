from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'home.html', {'name1': 'Ashkan', 'name2':'Zahra'})
