from django.conf.urls.defaults import *

urlpatterns = patterns('pinax.apps',
    url(r'^username_autocomplete/$', 'autocomplete_app.views.username_autocomplete_all', name='profile_username_autocomplete'),
    url(r'^$', 'profiles.views.profiles', name='profile_list'),
    url(r'^search/$', 'profiles.views.profiles', name="profile_list"),
    url(r'^(?P<username>[\w\._-]+)/$', 'profiles.views.profile', name='profile_detail'),
)
