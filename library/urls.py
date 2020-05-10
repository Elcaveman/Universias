from django.urls import path
from . import views as v
app_name = 'library'

urlpatterns = [
    #API data(must be in a seperate app)
    path('postsAPI/' , v.postsAPI , name='postsAPI'),

    #views
    path('',v.home,name='home'),
    path('posts/',v.posts,name='posts'),
    path('posts/<int:post_id>/',v.item,name='item_detail'),
    path('labs/',v.labs),
    path('teams/',v.teams),
    #tests
    path('posts_test/',v.posts_test , name='posts_test')
]