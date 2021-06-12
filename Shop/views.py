from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import locations,productCategoy,productShop
from django.contrib.auth import authenticate,login
from .forms import ModifiedUserForm,LocationsForm,CategoryForm,ShopForm,ProductForm

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
        form = ModifiedUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = ModifiedUserForm()
    return render(request,'Shop/register.html',{'form':form})

def userDashboard(request):
    return render(request,'Shop/dashboard.html')


def Locations(request):
    if request.method == 'POST':
        form= LocationsForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locationname']
            locations.objects.create(locationname=loc)
            return redirect('locations')

    locs = locations.objects.all()
    form = LocationsForm()
    return render(request,'Shop/locations.html',{'form':form,'locs':locs})


def productCategory(request):
    if request.method == 'POST':
        form= CategoryForm(request.POST)
        if form.is_valid():
            loc = form.cleaned_data['locationname']
            productCategoy.objects.create(locationname=loc)
            return redirect('category')


    cats = productCategoy.objects.all()
    form = CategoryForm()
    return render(request,'Shop/category.html',{'cats':cats,'form':form})

def shopDetail(request):
    name= request.user
    if request.method =='POST':
        pass

    form= ShopForm()
    print(name)
    return render(request,'Shop/shop.html',{'form':form})

def products(request):
    product=productShop.objects.all()
    form=ProductForm()
    return render(request,'Shop/products.html',{'form':form,'product':product})