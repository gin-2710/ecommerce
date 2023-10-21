from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'pages/home.html', {})

def landingView(request):
    return render(request, 'pages/landing-page.html', {})