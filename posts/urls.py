import django

from django.urls import path, include
from django.contrib import admin
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
    path('', views.post_list, name='post-list'),
    path('posts/new',views.post_create, name='post-create'),
    path('posts/<int:post_id>',views.post_detail, name='post-detail'),
    path('posts/<int:post_id>/edit',views.post_update, name='post-update'),
    path('posts/<int:post_id>/delete',views.post_delete, name='post-delete'),
    # path('posts/findmovie', views.findmovie, name='findmovie'),
    # path('posts/searchtitle',views.searchtitle, name='searchtitle'),
    path('top17',views.top17, name='top17'),
]

