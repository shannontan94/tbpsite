from django.conf.urls import patterns, include, url
import django

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'web.views.home', name='home'),
    url(r'^events/$', 'event.views.events'),
    url(r'^events/(?P<url>\w+)/$', 'event.views.event'),
    url(r'^cb_race/$', 'web.views.event_redirect', {'event_url': 'cb_race'}),
    url(r'^candidates/$', 'web.views.candidates'),
    url(r'^programs/$', 'web.views.programs'),
    url(r'^emcc/$', 'web.views.emcc'),
    url(r'^fe/$', 'web.views.fe'),
    url(r'^about/$', 'web.views.about'),
    url(r'^awards/$', 'web.views.awards'),
    url(r'^officers/$', 'web.views.officers'),
    url(r'^faculty/$', 'web.views.faculty'),
    url(r'^tutoring/$', 'web.views.tutoring'),
    url(r'^feedback/$', 'web.views.feedback'),
    url(r'^contact/$', 'web.views.contact'),
    url(r'^eligibility_list/$', 'web.views.eligibility_list'),
    url(r'^houses/$', 'web.views.houses'),
    # url(r'^app/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'web.views.logout'),
    url(r'^login$', 'web.views.login'),
    url(r'^profile$', 'web.views.profile'),
    url(r'^resume$', 'web.views.resume'),
    url(r'^interview$', 'web.views.interview'),
)
