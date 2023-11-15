from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('appWebsite/', views.sayHello, name='sayHello'),
    # path('appWebsite/', views.members, name='members'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('home/', views.home, name='home')
]