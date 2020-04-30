from django.urls import path
from . import views as v
app_name = 'library'

urlpatterns = [
    path('',v.home,name='home'),
    path('posts/',v.posts,name='posts'),
    path('posts/<int:post_id>/',v.item,name='item'),
    
]
