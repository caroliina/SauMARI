from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saumari.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       
    url(r'^saumariapp/', include('saumariapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
