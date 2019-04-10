from django.conf.urls import url
from crud import views

urlpatterns=[
    # url(r'^crud$',views.crud),

    url(r'^create$',views.create),
    url(r'^index$',views.index),
    url(r'^update$',views.update),
    url(r'^delete$',views.delete),
    url(r'^view$',views.view)
]
