from django.conf.urls import patterns, include, url
#from aste import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',include('aste_core.urls',namespace='aste_core')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),

)
