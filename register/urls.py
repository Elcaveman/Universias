from django.urls import path
from . import views as v
app_name = 'register'

urlpatterns = [
    path('login/',v.login_view, name='login'),
    path('signup/',v.signup, name='signup'),
    path('logout/',v.logout_view , name='logout'),
    path('profile/',v.display_user,name='user_profile'),
    path('profile/<int:user_id>/',v.display_profile, name='display_profile'),
    path('profile/update/',v.update_profile , name='update_profile'),
    
]
