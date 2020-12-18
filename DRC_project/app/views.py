from django.shortcuts import render
from .forms import SigninForm, SignupForm

# Create your views here.
def signin(request):
    if request.method=="POST":
        form = SigninForm(request.POST)
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            return redirect("myshop:home")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    context = {"form": form} 
    return render(request, "signin.html", context)

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User saved")
            return redirect("myshop:signin")
        else:
            messages.error(request, "Error in form")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "shop/signup.html", context)