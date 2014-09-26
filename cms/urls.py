from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cms.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/$', 'cms.views.about', name='about'),
    url(r'^contact/$', 'cms.views.contact', name='contact'),
    url(r'^thanks/$', 'cms.views.thanks', name='thanks'),
    url(r'^accounts/login/$', 'cms.views.login', name='login'),
    url(r'^accounts/loggedin/$', 'cms.views.loggedin', name='loggedin'),
    url(r'^accounts/logout/$', 'cms.views.loggedin', name='logout'),
    url(r'^accounts/register/$', 'cms.views.register', name='register'),
    url(r'^accounts/register/complete/$', 'cms.views.registration_complete', name='registration_complete'),
    url(r'^accounts/password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password_reset/mailed/'},
        name="password_reset"),
    (r'^accounts/password_reset/mailed/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/accounts/password_reset/complete/'}),
    (r'^accounts/password_reset/complete/$',
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^accounts/password_change/$',
            'django.contrib.auth.views.password_change',
            {'post_change_redirect' : '/accounts/password_change/done/'},
            name="password_change"),
        (r'^accounts/password_change/done/$',
            'django.contrib.auth.views.password_change_done'),
    url(r'^admin/', include(admin.site.urls)),
)
