'''
Created on 7 oct. 2017

@author: charlotteritter
'''
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]