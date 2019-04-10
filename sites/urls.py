from django.conf.urls import url
from sites import views

urlpatterns = [
    # url(r'^sites$', views.sites)
    url(r'^signup', views.signup),
    url(r'^signin$', views.signin),
    url(r'^logout$',views.sessionLogout),
    url(r'^$', views.home),
]