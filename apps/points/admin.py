from bme.apps.points.models import Point
from bme.apps.olwidget import admin

admin.site.register(Point, admin.custom_geo_admin(
    {'layers':['google.hybrid'],}))
