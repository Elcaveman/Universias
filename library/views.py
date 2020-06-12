import datetime

from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from . import models

from django.conf.urls import handler404 , handler500

from django.utils import timezone
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib import messages

from django.template import RequestContext
from .forms import PostForm
import json

from django.db import connection

handler404 = "library.views.view_404"
handler500 = "library.views.view_500"

#API data (switch to rest api afterwards)
@login_required
def postsAPI(request):
    #use values to convert to JSON
    posts_count = models.Post.objects.count()
    posts_queryset = models.Post.objects.all()
    posts_list = list(posts_queryset.values(
        'id','title','pub_type','owner','timestamp'
    ))
    #let's add the authors and their profile pics
    for i in range(len(posts_list)):
        author_list = list(posts_queryset[i].authors.all())
        posts_list[i]['authors'] = list(
            models.Profile.objects.filter(
                user__in = author_list
            ).values('pk','profil_pic')
        )
    #we can pass a non dict response by setting safe to FALSE!
    #why we call it safe? welp
    #?Before ECMAScript5 it was possible to poison the JavaScript Array constructor.
    return JsonResponse(posts_list, safe = False)

@login_required
def user_posts(request , user_id):
    #only difference between postsAPI and user_posts is the args + this line
    posts_queryset = models.Post.objects.filter(authors__pk = user_id)
    posts_list = list(posts_queryset.values(
        'id','title','pub_type','owner','timestamp'
    ))
    #let's add the authors and their profile pics
    for i in range(len(posts_list)):
        author_list = list(posts_queryset[i].authors.all())
        posts_list[i]['authors'] = list(
            models.Profile.objects.filter(
                user__in = author_list
            ).values('pk','profil_pic')
        )
    #we can pass a non dict response by setting safe to FALSE!
    #why we call it safe? welp
    #?Before ECMAScript5 it was possible to poison the JavaScript Array constructor.
    return JsonResponse(posts_list, safe = False)
@login_required
def charts(request):
    context = {}
    def raw_query(query):
        with connection.cursor() as cursor:
            cursor.execute(query)
            tuple_list = cursor.fetchall()#returns a list or rows(tuples)
            return tuple_list
        
    context['posts_by_type_monthly']=raw_query("""SELECT date_trunc('month', timestamp) AS post_month, pub_type ,count(*) as monthly_posts
        FROM public.library_post
        GROUP BY post_month, pub_type;""")[:10]
    
    context['posts_by_domaine_total'] = raw_query("""SELECT domaine ,count(id) as total_posts
        FROM public.library_post
        GROUP BY domaine;""")[:10]
    context['posts_by_revue_total'] = raw_query("""SELECT  rev.name,count(post.id) as total_posts
        FROM public.library_post as post
		Inner Join public.library_revue as rev
		On rev.id = post.revue_id
        GROUP BY rev.name;""")[:10]
    # pos = models.Post.objects.raw("""SELECT id,date_trunc('month', timestamp) AS post_month, pub_type ,count(*) as monthly_posts
    # FROM public.library_post
    # GROUP BY post_month, pub_type;""")
    # for elt in pos:
    #     print(elt)
    #TODO: not doing pub by lab for now till i figure out a secure way to handle posts linked to a labo to avoid fraud ..
    #?revue_id for revue//domaine//pub_type for type
    #TODO: I don't know if clauses are exploitable or not for sql injection so i stick with a static string
    #////////////////////////////////////////////////////////////////////
    return JsonResponse(context , safe=False)
#views
def home(request):
    user_count = models.Profile.objects.count()
    labs_count = models.Laboratory.objects.count()
    posts_count = models.Post.objects.count()
    if request.user.is_authenticated:
        # date_joined based query to get total new users!
        context = {
            'user_count': user_count,
            'labs_count': labs_count,
            'posts_count' : posts_count,
        }
        return render(request , 'library/dashboard.html' , context)
    else:
        contribs = models.Profile.objects.filter(position = "LC")
        context = {
            'contribs': contribs,
            'user_count': user_count,
            'labs_count': labs_count,
            'posts_count' : posts_count,
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
    # we put 13 posts in a page
    posts_count = models.Post.objects.count()
    
    
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

#!Error page handler NOT WORKINGs
def view_404(request):
    return render(request , 'library/404.html')

def view_500(request):
    return render(request , 'library/500.html')


@login_required
def create_post_view(request):
    if request.POST:
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            #create the post instance but do not save it yet since we need to add an owner
            post_object = form.save(commit=False)
            post_object.owner = request.user.profile
            post_object.save()
            #when using commit = False we need to make sure we use form.save_m2m() to save ManytoMany fields
            form.save_m2m()
            #an owner is an author aswell
            #we add it this late to avoid ValueError because the object
            #needs to have a value for field "id" before this many-to-many relationship can be used.
            post_object.authors.add(request.user.profile)
            post_object.save()
            messages.success(request , "Post created successfully")
            return redirect('/profile/')
    else:
        form = PostForm()
    return render(request , 'library/add_post.html' ,{'form':form})

@login_required
def delete_post_view(request , post_id):
    try:
        post = models.Post.objects.filter(id=post_id)[0]
    except:
        messages.error(request,'This post doesn\'t exist')
        return redirect('/profile/')
    if request.user.pk == post.owner.pk:
        #? what's the diference between clear and remove?
        post.delete()
        messages.success(request,'Post deleted sucessfully')
    else:
        messages.error(request,'You can\'t delete a post that isn\'t your own!')
    return redirect('/profile/')

@login_required
def edit_post_view(request, post_id):
    try:
        post = models.Post.objects.filter(id=post_id)[0]
    except:
        messages.error(request,'This post doesn\'t exist')
        return redirect('/profile/')
    if request.user.pk == post.owner.pk:
        if request.method == 'POST':
            form = PostForm(request.POST , request.FILES,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Post edited sucessfully')
                return redirect('/profile/')
            else:
                if form.errors:#errors is a dictionnary
                    base = {'pub_type':'Invalid Publication Type'}
                    for error in form.errors:
                        try :
                            messages.error(request,base[error])
                        except:
                            pass
                    
        else:
            form = PostForm(instance=post)
        return render(request , 'library/add_post.html',{'form':form})
    else:
        messages.error(request,'You can\'t edit a post that isn\'t your own!')
    return redirect('/profile/')