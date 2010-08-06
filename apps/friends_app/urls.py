from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'bme.apps.friends_app.views.friends', name='invitations'),
    url(r'^contacts/$', 'bme.apps.friends_app.views.contacts',  name='invitations_contacts'),
    url(r'^accept/(\w+)/$', 'bme.apps.friends_app.views.accept_join', name='friends_accept_join'),
)
