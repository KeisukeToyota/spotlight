from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'report', views.report, name='report'),
    url(r'user', views.user_confirmation, name='user_confirmation')
]