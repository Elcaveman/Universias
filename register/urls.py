from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as v
#beware not to add an app_name ! else you need to modify every {%url %} in the templates
urlpatterns = [
    path('login/',v.login_view, name='login'),
    path('signup/',v.signup, name='signup'),
    path('logout/',v.logout_view , name='logout'),
    path('profile/',v.display_user,name='user_profile'),
    path('profile/<int:user_id>/',v.display_profile, name='display_profile'),
    path('profile/update/',v.update_profile , name='update_profile'),
    
    path('reset_password/' , auth_views.PasswordResetView.as_view(
        template_name='register/recup/reset_password.html'),
    name = "reset_password"),
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name='register/recup/password_reset_done.html')
    ,name='password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name='register/recup/password_reset_confirm.html') ,
    name='password_reset_confirm'),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='register/recup/password_reset_complete.html'),
    name='password_reset_complete'),
    
]
