from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^mail/$', views.sendSimpleEmail, name='sendSimpleEmail'),
    url(r'^verify/$', views.fetchquery, name='fetchquery'),
    
]