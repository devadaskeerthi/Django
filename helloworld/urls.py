from django.contrib import admin
from django.urls import path,include
from helloworld import views


urlpatterns = [
    
    #path('',views.index)
    path('',views.index),
    path('index',views.index),
    path('login',views.login),
    path('register',views.register),
    path('pages',views.pages),
    path('userhome',views.userhome),
    path('edit',views.edit),
    path("mygallery",views.mygallery),
    path("image",views.image),
    path("audio",views.audio),
    path("video",views.video)

]
