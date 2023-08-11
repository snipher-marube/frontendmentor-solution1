from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def pricing(request):
    return render(request, 'app/pricing.html')

def addons(request):
    return render(request, 'app/addons.html')

def summary(request):
    return render(request, 'app/summary.html')

def success(request):
    return render(request, 'app/success.html')
