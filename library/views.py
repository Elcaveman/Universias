from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('home')

def posts(request):
    return HttpResponse('posts')

def item(request , post_id):
    return HttpResponse('post %d'%post_id)
