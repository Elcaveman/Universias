from django.urls import path
from . import views as v
app_name = 'library'

urlpatterns = [
    #API data(must be in a seperate app)
    path('postsAPI/' , v.postsAPI , name='postsAPI'),
    path('user_posts/<int:user_id>/',v.user_posts , name='user_posts'),
    #views
    path('',v.home,name='home'),
    path('posts/',v.posts,name='posts'),
    path('posts/<int:post_id>/',v.item,name='item_detail'),
    path('labs/',v.labs),
    path('teams/',v.teams),

    path('create_post/' , v.create_post_view , name='create_post'),
    path('delete_post/<int:post_id>/' , v.delete_post_view , name='delete_post'),
    path('edit_post/<int:post_id>/' , v.edit_post_view , name='edit_post'),
    
]