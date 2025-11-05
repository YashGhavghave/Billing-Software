from django.shortcuts import render

def home(request):
    return render(request, 'KUBS_home.html')