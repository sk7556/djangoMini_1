from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def friends(request):
    return render(request, 'friends.html')