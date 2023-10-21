from django.urls import path
from .views import homeView, landingView

urlpatterns = [
    path('', landingView, name="landing"),
    path('home/', homeView, name = "home"),
]