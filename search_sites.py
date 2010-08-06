import haystack
from django.conf import settings

if not getattr(settings,'INITIAL_SYNC', False):
    haystack.autodiscover()
else:
    import logging
    log = logging.getLogger('haystack')
    log.warn('Skipping haystack loading until settings.INITIAL_SYNC=False')

