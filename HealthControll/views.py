from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    if not request.COOKIES.get('is_login') == 'True':
        return redirect('/login/')
    return render(request, 'index.html')

def record(request):
    if request.method == "GET":
        return render(request, 'record.html')
    age = request.POST.get('age')
    weight = request.POST.get('weight')
    height = request.POST.get('height')
    target = request.POST.get('target')
    gender = request.POST.get('sex')
    print(age, weight, height, target, gender)
    return redirect('/index/')
