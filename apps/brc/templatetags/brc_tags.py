from django import template
register = template.Library()

from bme.apps.olwidget.widgets import MapDisplay

register.inclusion_tag('')
def brc_test():
	return locals()

register.tag('brc_test', brc_test)
