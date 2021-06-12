from django.urls import path
from .views import loginUser,registerUser,userDashboard,Locations,productCategory,shopDetail,products


urlpatterns = [
    path('',loginUser,name='login'),
    path('dashboard/',userDashboard,name='userDashboard'),
    path('register/',registerUser,name='registerUser'),
    path('locations/',Locations,name='locations'),
    path('category/', productCategory, name='category'),
    path('shop/',shopDetail, name='shopDetail'),
    path('products/',products,name='products')

]