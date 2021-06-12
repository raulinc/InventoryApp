from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

#Create your views here.


def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('userDashboard')
    form =AuthenticationForm()
    return render(request,'Shop/Login.html',{'form':form})

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request,'Shop/register.html',{'form':form})

def userDashboard(request):
    return render(request,'Shop/dashboard.html')