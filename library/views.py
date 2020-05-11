import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . import models

from django.utils import timezone
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

import json
#API data (switch to rest api afterwards)
@login_required
def postsAPI(request):
    #use values to convert to JSON
    posts_queryset = models.Post.objects.all().values(
        'id','title','pub_type','authors','timestamp'
    )
    posts_list = list(posts_queryset)
    #we can pass a non dict response by setting safe to FALSE!
    #why we call it safe? welp
    #?Before ECMAScript5 it was possible to poison the JavaScript Array constructor.
    return JsonResponse(posts_list, safe = False)

@login_required
def user_posts(request , user_id):
    posts_list = list(models.Post.objects.filter(authors__pk = user_id).values(
        'id','title','pub_type','authors','timestamp'
    ))
    return JsonResponse(posts_list, safe = False)

#views
def home(request):
    rp = models.Post.objects.filter(
        timestamp__gte=timezone.now() - datetime.timedelta(days=7))
    context = {
        'recent_posts': rp,
    }
    return render(request, 'library/homepage.html', context)
@login_required
def posts_test(request):
    return render(request , 'library/posts_table.html')

@login_required
def posts(request):
    #* see posts_test()
    #! note about this one:
    #?  1- pagination done in JS
    #?  2- passing data using an API instead of jinja + context
    #?  3- make responsive search bar and filters

    posts_queryset = models.Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_queryset, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if the user insput is not an integer point to 1st page
        posts = paginator.page(1)
    except EmptyPage:
        #if we surpass the available nbr of pages point back to the lasters one
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'library/posts_table.html', { 'posts': posts })

@login_required
def item(request , post_id):
    try:
        post = models.Post.objects.get(id=post_id)
        return render(request, 'library/single_post.html', {'post':post})

    except models.Post.DoesNotExist:
        raise Http404

def teams(request):
    return HttpResponse('teams')

def labs(request):
    return HttpResponse('labs')