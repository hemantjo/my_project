from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def signin(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email,  password=password)
        if user is not None:
            login(request, user)
            return redirect("myapp:signup")
        else:
            return render(request, 'signin.html', {"not_authenticated": True})
    return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_signup = User(email=email, password=password)
            user_signup.set_password(password)
            user_signup.save()
        except Exception as e:
            print(e)
        return redirect("myapp:signin")
    return render(request, "signup.html")