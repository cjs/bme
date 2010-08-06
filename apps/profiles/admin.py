from django.contrib import admin
from bme.apps.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['user__username', 'name', 'about', 'location']

admin.site.register(Profile, ProfileAdmin)

