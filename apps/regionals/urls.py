from django.conf.urls.defaults import *

urlpatterns = patterns('bme.apps',
        url(r'^$', 'regionals.views.regionals', name="regional_list"),
    )
