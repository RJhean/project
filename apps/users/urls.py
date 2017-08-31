from django.conf.urls import url

from . import views

app_name= 'users'

urlpatterns = [

    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
]