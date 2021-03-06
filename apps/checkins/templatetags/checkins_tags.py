from django import template
register = template.Library()

from django.contrib.contenttypes.models import ContentType
from olwidget.widgets import MapDisplay

from checkins.models import CheckIn
import datetime


@register.inclusion_tag('checkins/checkins_add_form.html')
def add_checkin_for_instance(model_instance, user):
    ''' make a form to post a new checkin

    {% add_checkin_for_instance MyObject request.user %}
    '''

    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    c = CheckIn.objects.filter(
            content_type=ct,
            object_id = obj_id,
            owner=user,
            datetime__gte=datetime.datetime.now()-datetime.timedelta(seconds=2)
    )

    if not c:
        c = CheckIn.objects.filter(
            owner=user,
            datetime__gte=datetime.datetime.now()-datetime.timedelta(seconds=2)
        )

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('checkins/link.html')
def link_to_checkins_for(model_instance, css_class=''):
    ''' link to see the checkins for the object

    {% link_to_checkins_for myModelInstance 'css_class' %}
    '''
    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()


@register.inclusion_tag('checkins/checkins_latest_for.html')
def latest_checkins_for_instance(model_instance, num=5):
    ''' Show the latest checkins for your model

    {% latest_checkins_for_instance theme_camp %}
    '''

    ct = ContentType.objects.get_for_model(model_instance)

    checkins = CheckIn.objects.filter(
            content_type = ct, object_id = model_instance.id
    )[:num]

    if CheckIn.objects.filter(
            content_type = ct,
            object_id = model_instance.id).count() > num:
        more = True

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

#TODO: Add last checkin for user

@register.inclusion_tag('points/add_change_link.html')
def add_change_link(model_instance, css_class="add-point"):

    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    if Point.objects.filter(content_type = ct, object_id=obj_id):
        point = Point.objects.filter(content_type = ct, object_id=obj_id)[0]

    else:
        point = None

    app_label = model_instance._meta.app_label
    model_name = model_instance._meta.module_name

    return locals()

@register.inclusion_tag('points/show_google_map_single.html')
def show_google_map(model_instance, css_id="default-map"):
    ''' Turn a DOM element into a map using the google API

    {% show_google_map model_instance css_id %}
    Note that this returns the *latest* point that has been
    added to the model instance.
    '''
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    if Point.objects.filter(content_type = ct, object_id=obj_id):
        point = Point.objects.filter(content_type = ct, object_id=obj_id)[0]
    else:
        return None

    return locals()

@register.inclusion_tag('points/show_google_map_multi.html')
def show_google_all(model_instance, css_id="default-map"):
    ''' Shows all points given a model_instance

    {% show_google_all model_instance css_id %}
    '''

    # FIXME, we should factor out some of this wet-ness
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    if Point.objects.filter(content_type = ct, object_id=obj_id):
        points = Point.objects.filter(content_type = ct, object_id=obj_id)
    else:
        return None

    return locals()



@register.inclusion_tag('points/show_ol_map.html')
def show_ol_map(model_instance):
    ''' Takes a model instance and returns display of all points html

    {% show_ol_map model_instance %}
    '''
    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    points = Point.objects.filter(content_type = ct, object_id=obj_id)

    map = MapDisplay( fields=[p.point for p in points],
            map_options = {
                    'map_style':{'width':'360px', 'height':'240px',},
                    'layers': ['osm.mapnik','google.hybrid'],
            }
    )

    return locals()

@register.inclusion_tag('points/show_ol_media.html')
def show_ol_media(model_instance):
    ''' What needs to be in head for show_ol_map tag

    '''
    r = show_ol_map(model_instance)
    return r

@register.inclusion_tag('points/show_ol_map.html')
def show_latest_point_ol(model_instance):
    ''' Takes model instance and displays the latest point

    '''

    ct = ContentType.objects.get_for_model(model_instance)
    obj_id = model_instance.id

    if Point.objects.filter(content_type = ct, object_id=obj_id):
        point = Point.objects.filter(content_type = ct, object_id=obj_id)[0]
    else:
        point = None

    if point:
        map = MapDisplay( fields=[ point.point,],
            map_options = {
                    'map_style':{'width':'360px', 'height':'240px',},
                    'layers': ['osm.mapnik'],
                    'zoom': point.zoom,
            }
        )
    else:
        map = MapDisplay(
            map_options = {
                    'map_style':{'width':'360px', 'height':'240px',},
                    'layers': ['osm.mapnik'],
                    'zoom': 14,
            }
        )

    return locals()

@register.inclusion_tag('points/show_ol_media.html')
def show_latest_point_ol_media(model_instance):
    r = show_latest_point_ol(model_instance)
    return r


@register.inclusion_tag('points/show_ol_map.html')
def latest_for_queryset_map(queryset):
    ''' Show the latest point for each instance in a qs

    In head::

        {% latest_for_queryset_media queryset %}

    In body::

        {% latest_for_queryset_map queryset %}

    '''

    ct = ContentType.objects.get_for_model(queryset[0])
    points = []

    for m in queryset:
        if Point.objects.filter( content_type=ct, object_id=m.id ):
            p = Point.objects.filter( content_type=ct, object_id=m.id )[0]
            points.append(p)

        else:
            continue

    map = MapDisplay( fields=[ p.point for p in points ],
            map_options = {
                    'map_style':{'width':'240px', 'height':'160px',},
                    'layers': ['osm.mapnik','google.hybrid'],
            }
    )

    return locals()

@register.inclusion_tag('points/show_ol_media.html')
def latest_for_queryset_media(queryset):
    r = latest_for_queryset_map(queryset)
    return r

@register.inclusion_tag('points/show_google_map_multi.html')
def latest_for_queryset_google(queryset, css_id="latest_for_queryset"):
    ''' Show the latest point for each member of a queryset

    In head::

        {% latest_for_queryset_google queryset "css_id" %}

    In body something like::

        <div id="css_id" style="width:100%; height:300px;"></div>

    '''

    ct = ContentType.objects.get_for_model(queryset[0])
    points = []

    for m in queryset:
        if Point.objects.filter( content_type=ct, object_id=m.id ):
            p = Point.objects.filter( content_type=ct, object_id=m.id )[0]
            points.append(p)

        else:
            continue

    return locals()

@register.inclusion_tag('points/show_google_map_multi.html')
def google_show_points_owned_by(user, css_id):
    ''' Show the points that are owned by a given user

    {% google_show_points_owned_by user "css_id" %}
    '''

    points = Point.objects.filter(owner=user)

    return locals()





