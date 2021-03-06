from django.conf.urls.defaults import *

urlpatterns = patterns('',
     url(r'^$', 'brc.views.index', name="index"),
     url(r'^(?P<year_year>\d{4})/$', 'brc.views.year_info', name="year_info"),
     url(r'^(?P<year_year>\d{4})/sikrit_map/$', 'brc.views.sikrit_map', name="sikrit_map"),
     url(r'^(?P<year_year>\d{4})/map/$', 'brc.views.map', name="map"),
     url(r'^(?P<year_year>\d{4})/mobile_map/$', 'brc.views.mobile_map', name="mobile_map"),
     url(r'^(?P<year_year>\d{4})/globe/$', 'brc.views.globe', name="globe"),
     url(r'^(?P<year_year>\d{4})/themecamp/(?P<theme_camp_id>\d{1,4})/$', 'brc.views.themecampid', name="themecamp"),
     url(r'^(?P<year_year>\d{4})/themecamps/$', 'brc.views.themecamps', name="themecamps"),
     url(r'^themecamp/(?P<theme_camp_id>\d{1,4})/$', 'brc.views.themecampuuid', name="themecamp"),
     url(r'^(?P<year_year>\d{4})/art_installation/(?P<art_installation_id>\d{1,4})/$', 'brc.views.art_installation_id', name="art_installation"),
     url(r'^(?P<year_year>\d{4})/art_installations/$', 'brc.views.art_installations', name="art_installations"),
     url(r'^art_installation/(?P<art_installation_id>\d{1,4})/$', 'brc.views.art_installation_uuid', name="art_installation"),
     url(r'^(?P<year_year>\d{4})/art_car/(?P<art_car_id>\d{1,4})/$', 'brc.views.art_car_id', name="art_car"),
     url(r'^(?P<year_year>\d{4})/art_cars/$', 'brc.views.art_cars', name="art_cars"),
     url(r'^(?P<year_year>\d{4})/playa_events/$', 'brc.views.playa_events_home', name="playa_events"),
     url(r'^(?P<year_year>\d{4})/csv_onetime/$', 'brc.views.csv_onetime', name="csv_onetime"),
     url(r'^(?P<year_year>\d{4})/csv_all_day_onetime/$', 'brc.views.csv_all_day_onetime', name="csv_all_day_onetime"),
     url(r'^(?P<year_year>\d{4})/csv_repeating/$', 'brc.views.csv_repeating', name="csv_repeating"),
     url(r'^(?P<year_year>\d{4})/csv_all_day_repeating/$', 'brc.views.csv_all_day_repeating', name="csv_all_day_repeating"),
     url(r'^(?P<year_year>\d{4})/playa_events/my_events/$', 'brc.views.playa_events_view_mine', name="playa_events_view_mine"),
     url(r'^(?P<year_year>\d{4})/playa_events/(?P<playa_day>\d{1})/$', 'brc.views.playa_events_by_day', name="playa_events_by_day"),
     url(r'^(?P<year_year>\d{4})/playa_event/create/$', direct_to_template, {"template": "disabled.html"}, name="playa_event_add"),
     #url(r'^(?P<year_year>\d{4})/playa_event/create/$', 'brc.views.create_or_edit_event', name="playa_event_add"),
     url(r'^(?P<year_year>\d{4})/playa_event/create/(?P<playa_day>\d{1})/$', direct_to_template, {"template": "disabled.html"}, name="playa_event_add"),
     #url(r'^(?P<year_year>\d{4})/playa_event/create/(?P<playa_day>\d{1})/$', 'brc.views.create_or_edit_event', name="playa_event_add"),
     url(r'^(?P<year_year>\d{4})/playa_event/edit/(?P<playa_event_id>\d+)/$', direct_to_template, {"template": "disabled.html"}, name="playa_event_edit"),
     #url(r'^(?P<year_year>\d{4})/playa_event/edit/(?P<playa_event_id>\d+)/$', 'brc.views.create_or_edit_event', name="playa_event_edit"),
     url(r'^(?P<year_year>\d{4})/playa_event/delete/(?P<playa_event_id>\d+)/$', direct_to_template, {"template": "disabled.html"}, name="playa_event_delete"),
     #url(r'^(?P<year_year>\d{4})/playa_event/delete/(?P<playa_event_id>\d+)/$', 'brc.views.delete_event', name="playa_event_delete"),
     url(r'^(?P<year_year>\d{4})/playa_event/delete_occurrence/(?P<occurrence_id>\d+)/$', direct_to_template, {"template": "disabled.html"}, name="occurrence_delete"),
     #url(r'^(?P<year_year>\d{4})/playa_event/delete_occurrence/(?P<occurrence_id>\d+)/$', 'brc.views.delete_occurrence', name="occurrence_delete"),
     url(r'^(?P<year_year>\d{4})/playa_event/(?P<playa_event_id>\d+)/$', 'brc.views.playa_event_view', name="playa_event_view"),
     url(r'^playa_event/(?P<playa_event_id>\d+)/$', 'brc.views.playa_event_view_uuid', name="playa_event_view"),
     url(r'^(?P<year_year>\d{4})/playa_event/(?P<playa_event_id>\d+)/(?P<playa_occurrence_id>\d+)/$', 'brc.views.playa_occurrence_view', name="playa_occurrence_view"),
     url(r'^(?P<year_year>\d{4})/playa_event/edit/(?P<playa_event_id>\d+)/(?P<playa_occurrence_id>\d+)/$', direct_to_template, {"template": "disabled.html"}, name="playa_occurrence_edit"),
     #url(r'^(?P<year_year>\d{4})/playa_event/edit/(?P<playa_event_id>\d+)/(?P<playa_occurrence_id>\d+)/$', 'brc.views.playa_occurrence_view', name="playa_occurrence_edit"),
     url(r'^(?P<year_year>\d{4})/playa_event/add_occurrence/(?P<playa_event_id>\d+)/$', 'brc.views.playa_occurrence_view', name="playa_occurrence_add"),
     url(r'^(?P<year_year>\d{4})/(?P<hour>\d{1,2}):(?P<minute>\d{1,2})/(?P<street>[a-z-]{0,50})/$', 'brc.views.neighborhood', name="neighborhood"),
     url(r'^geocoder/(?P<year_year>\d{4})/(?P<hour>\d{1,2}):(?P<minute>\d{1,2})/(?P<street>[a-z-]{0,50})/$', 'brc.views.geocoder', name="geocoder"),
     url(r'^swingtime/', include('swingtime.urls')),
     url(r'^search/', include('haystack.urls')),
)

#from haystack.forms import ModelSearchForm
#from haystack.query import SearchQuerySet
#from haystack.views import SearchView

#urlpatterns += patterns('haystack.views',
#    url(r'^brcsearch/', SearchView(
#        template='search/search.html',
#        form_class=ModelSearchForm
#    ), name='haystack_search'),
#)
