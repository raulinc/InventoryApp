from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import shopDetail,productShop

class ModifiedUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class LocationsForm(forms.Form):
    locationname = forms.CharField(max_length=30)

class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=30)

class ShopForm(forms.ModelForm):
    class Meta:
        model = shopDetail
        fields = ['shopName','address','shopLocation']

class ProductForm(forms.ModelForm):
    class Meta:
        model = productShop
        fields = ['productname','productDescription','productCategory','price','shop']