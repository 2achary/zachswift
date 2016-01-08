from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.home', name='home'),
    url(r'^about', 'portfolio.views.about', name='about'),
    url(r'^contact', 'portfolio.views.contact', name='contact'),
    url(r'^resume', 'portfolio.views.resume', name='resume'),
    url(r'^lightbox', 'portfolio.views.lightbox', name='lightbox'),
    url(r'^taskdaddy', 'portfolio.views.taskdaddy', name='taskdaddy'),
    url(r'^spoiler', 'portfolio.views.spoiler', name='spoiler'),
    url(r'^projects', 'portfolio.views.projects', name='projects'),
    url(r'^sms', 'portfolio.views.sms', name='sms'),


    url(r'^admin/', include(admin.site.urls)),
)
