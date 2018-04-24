from django.shortcuts import render
from . models import Project

'''
displays our home page and loads in our stored Project models from the DB.
'''
def home(request):
    projects = Project.objects
    return render(request, 'mypage/home.html', {'projects':projects})

def aboutme(request):
    return render(request, 'mypage/aboutme.html')