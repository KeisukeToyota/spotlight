from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'tweets', views.tweet_index, name='tweet_list'),
    url(r'report', views.report, name='report'),
    url(r'users', views.user_index, name='user_list'),
    url(r'user/', views.user_confirmation, name='user_confirmation'),
    url(r'version', views.version_check, name='version_check'),
    url(r'user_csv', views.user_csv, name='user_csv'),
]