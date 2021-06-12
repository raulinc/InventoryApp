from django.urls import path
from .views import loginUser,registerUser,userDashboard


urlpatterns = [
    path('',loginUser,name='login'),
    path('dashboard/',userDashboard,name='userDashboard'),
    path('register/',registerUser,name='registerUser'),
]