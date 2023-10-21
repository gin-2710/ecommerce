from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm


# Create your views here.
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})   

def registerView(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            print("User saved successfully")
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=CustomUserCreationForm()   
    return render(request,'user/register.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('landing')
    