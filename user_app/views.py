from django.shortcuts import render,redirect
from django.views.generic import View
from user_app.models import User
from user_app.forms import *
from django.contrib.auth import authenticate,login
# Create your views here.
class Registerview(View):
    def get(self,request):
        form = Registerform()
        return render(request,"register.html",{"form":form})
    
    def post(self,request):
        form = Registerform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            User.objects.create_user(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password")
            )
            return render(request,"register.html")
        return render(request,"register.html")

class Loginview(View):
    def get(self,request):
        form = Loginform()
        return render(request,"login.html",{"form":form})
    
    