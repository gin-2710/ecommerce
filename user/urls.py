from django.urls import path
from .views import loginView, registerView, logoutView

urlpatterns = [
    path('login/', loginView , name='loginForm'),
    path('register/', registerView, name = 'registerForm'),
    path('logout/', logoutView, name = 'logout'),
]