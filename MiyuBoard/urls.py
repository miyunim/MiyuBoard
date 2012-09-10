from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from board.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
        {'template': 'registration/register_success.html'}),
    # Examples:
    # url(r'^$', 'MiyuBoard.views.home', name='home'),
    # url(r'^MiyuBoard/', include('MiyuBoard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
