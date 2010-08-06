from django.contrib.contenttypes import generic
from django.contrib import admin
from bme.apps.swingtime.models import *

#===============================================================================
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('label', 'abbr')


#===============================================================================
class NoteAdmin(admin.ModelAdmin):
    list_display = ('note', 'created')


#===============================================================================
class OccurrenceInline(admin.TabularInline):
    model = Occurrence
    extra = 1


#===============================================================================
class EventNoteInline(generic.GenericTabularInline):
    model = Note
    extra = 1


#===============================================================================
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'description')
    list_filter = ('event_type', )
    search_fields = ('title', 'description')
    inlines = [EventNoteInline, OccurrenceInline]


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Note, NoteAdmin)