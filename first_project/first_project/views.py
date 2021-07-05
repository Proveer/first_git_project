from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def result(request):
    return render(request,'result.html')

def result2(request):
    first_name = request.GET['firstname']
    last_name = request.GET.get('lastname')
    return render(request,'result2.html', {'home_input':first_name})