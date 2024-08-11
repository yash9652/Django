from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.post_list,name='post_list'),
    #path("post/<int:pk>",views.post_details,name="post_details"),
    path('post/<slug:slug>/',views.post_details,name="post_details"),
    path('add',views.post_add,name="post_add"),
]