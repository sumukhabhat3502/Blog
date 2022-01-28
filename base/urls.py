from os import name
from django.urls import path, include

from .models import Category
from . import views
from .views import CommentAdd, Detail, Home, PostAdd, Update_Post, Delete_Post, CategoryAdd, CategoryView, Like
urlpatterns = [
    # path('',views.home,name='home'),
    # Because class based views are in 'view.py'
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', Detail.as_view(),
         name='detail'),  # pk is primary-key
    path('postadd/', PostAdd.as_view(), name='add_post'),
    path('article/edit/<int:pk>', Update_Post.as_view(), name='edit'),
    path('article/<int:pk>/delete', Delete_Post.as_view(), name='delete'),
    path('add_category', CategoryAdd.as_view(), name='Add_Category'),
    path('category/<str:cat>/', CategoryView, name='category'),
    path('like/<int:pk>', Like, name='like_post'),
    path('article/<int:pk>/comment', CommentAdd.as_view(), name='Add_comment'),

    # path('user-profile/',),
]
