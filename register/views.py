from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm , UserExtrasForm , ProfileForm , AuthenticationForm , UserCreationForm

from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

from django.utils.datastructures import MultiValueDictKeyError
from . import models


#just a litle decorator that checks if user is loged in if he is goes to profile else it performs the view
def no_user_required(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('/profile/')
        else:
            return view(request)
    return wrapper

@no_user_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = authenticate(request , **form.cleaned_data)
            if user is None:
                messages.error(request,'Login failed! password or username is incorrect')
            else:
                messages.success(request , 'Welcome {}'.format(form.cleaned_data.get('username')))
                login(request,user)
                return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request , f"{msg} : {form.error_messages[msg]}")
    else:
        form = AuthenticationForm()
    return render(request , 'register/login.html' , {'form':form})    

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    messages.info(request,'Logout successful!')
    return redirect('/')

@no_user_required
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user_extras = UserExtrasForm(request.POST)
        #need to add the request.FILES to get the profile_pic
        profile_form = ProfileForm(request.POST , request.FILES)
        pic_validator = False
        try:
            if request.FILES['profil_pic'].size > 20 * 1024 * 1024 :
                messages.error(request,"Picture size is over 20Mb")
            else:
                pic_validator = True
        except MultiValueDictKeyError:
            pic_validator = None
        
        if user_form.is_valid() and user_extras.is_valid() and profile_form.is_valid() and pic_validator:
            user = user_form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            
            user.first_name = user_extras.cleaned_data['first_name']
            user.last_name = user_extras.cleaned_data['last_name']
            user.email = user_extras.cleaned_data['email']
            # user.profile.profil_pic = request.FILES.get('profil_pic',None)
            #don't forget the enc type on the form !!
            user.save()
            # to pass MultiValueDictKeyError i need to use a get method
            
            profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)  # Reload the profile form with the profile instance
            #profile_form.full_clean()# Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()#Gracefully save the form

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            messages.success(request,"New Account Created!")
            messages.info(request,f"Welcome {user}!")
            login(request, user)
            return redirect('/')
        else:
            #handling the errors with the built in django messages!#! with jinja2
            pass
    else:
        user_form = UserCreationForm()
        user_extras = UserExtrasForm()
        profile_form = ProfileForm()

    context = {
        'user_form':user_form,
        'user_extras':user_extras,
        'profile_form':profile_form,}
    return render(request, 'register/signup.html', context)

@login_required(login_url='/login/')
def display_profile(request,user_id):
    try:
        user = models.Profile.objects.filter(pk=user_id)[0]
        return render(request,'register/profile_display.html',{'user_profile':user})
    except :
        raise Http404
    
@login_required(login_url='/login/')
def display_user(request):
    user_id = request.user.id
    return display_profile(request , user_id)


@login_required(login_url='/login/')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('/profile/')
        else:
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'register/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

