from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^parandustood$', views.parandustood, name='parandustood'),
    url(r'^trenniriided$', views.trenniriided, name='trenniriided'),
]