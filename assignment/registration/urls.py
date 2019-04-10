from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^registration$', views.register),
    url(r'^thanks$',views.thanks),
    url(r'^login$', views.login)
]
