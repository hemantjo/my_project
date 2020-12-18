from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Uploads
from django.views.generic import TemplateView
# from django.contrib.gis.geoip import GeoIP


# Create your views here.
def signin(request):
    try:
        if request.method=="POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email,  password=password)
            if user is not None:
                login(request, user)
                return redirect("myapp:home")
            else:
                return render(request, 'signin.html', {"not_authenticated": True})
    except LockedOut:
        return render(request, 'signin.html', {"locked_out": True})
    return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # g = GeoIP()
        # g.city(ip)
        # import code; code.interact(local=dict(globals(), **locals()))        
        try:
            user_signup = User(email=email, password=password)
            user_signup.set_password(password)
            user_signup.save()
        except Exception as e:
            print(e)
        return redirect("myapp:signin")
    return render(request, "signup.html")

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['uploads'] = Uploads.objects.filter(user=self.request.user)
        return context

def upload(request):
    if request.method == 'POST':
        file_name = request.POST.get('name')
        image = request.FILES['img']
        try:
            user_uploads = Uploads(user=request.user, file_name=file_name, image=image)
            user_uploads.save()
        except Exception as e:
            print(e)
        return redirect("myapp:home")
    return render(request, "home.html")

def signout(request):
    logout(request)
    return redirect('myapp:signin')