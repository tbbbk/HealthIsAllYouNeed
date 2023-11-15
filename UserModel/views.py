from django.shortcuts import redirect, render
from UserModel.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)

    if not user:
        print("查无此人")
        return render(request, 'login.html', {'error': '用户名或密码错误'})
    else:
        rep = redirect("/index/")
        rep.set_cookie("is_login", True)
        return rep


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
        return render(request, 'register.html', {'error': '用户名已被使用'})

    new_user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    return redirect('/login/')  
