
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('products/',views.products,name="products"),
    

]
