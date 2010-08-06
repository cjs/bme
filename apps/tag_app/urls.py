from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # all tags
    url(r'^(?P<tag>.+)/$', 'bme.apps.tag_app.views.tags', name='tag_results'),
)
