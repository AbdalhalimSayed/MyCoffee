from django.urls import path
from . import views

urlpatterns = [
    path('',views.signIn , name='signin'),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path('logOut', views.LogOut,name="LogOut")
]
