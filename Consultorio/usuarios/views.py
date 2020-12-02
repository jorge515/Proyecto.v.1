from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login ,logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
       HttpResponseRedirect (reverse,("login"))
    return render(request, "usuarios/usuarios.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"usuarios/login.html", {
                "mensaje": "Credenciales no validas" 
                })
    return(request,"usuarios/login.html")

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html",{ 
        "mensaje":"Usted se ha desctonectado con exito"
    })
        