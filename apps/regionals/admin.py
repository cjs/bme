from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from bme.apps.regionals.models import Regional

class RegionalAdmin(OSMGeoAdmin):
    list_display = ('name',)

#class RegionalAdmin(OSMGeoAdmin):
#    list_display = ('title', )

admin.site.register(Regional, RegionalAdmin)
#admin.site.register(Topic, TopicAdmin)
