from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm,UserExtrasForm,ProfileForm

from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

#just a litle decorator that checks if user is loged in if he is goes to profile else it performs the view
def no_user_required(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('/profile/')
        else:
            return view(request)
    return wrapper

def login_view(request):
    return HttpResponse('login')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('/')

@no_user_required
def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_extras = UserExtrasForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and user_extras.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            user.first_name = user_extras.cleaned_data['first_name']
            user.last_name = user_extras.cleaned_data['last_name']
            user.email = user_extras.cleaned_data['email']

            profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()# Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()#Gracefully save the form

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        user_extras = UserExtrasForm()
        profile_form = ProfileForm()
    context = {
        'user_form':user_form,
        'user_extras':user_extras,
        'profile_form':profile_form,
    }
    return render(request, 'register/signup.html', context)

@login_required(login_url='/login/')
def display_profile(request,user_id):
    return HttpResponse('profile %d'%user_id)

@login_required(login_url='/login/')
def display_user(request):
    user_id = request.user.id
    return display_profile(request , user_id)


@login_required(login_url='/login/')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        user_extras = UserExtrasForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('/profile/')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })