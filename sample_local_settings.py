PINAX_ROOT='../pinax'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'bme'
DATABASE_USER = 'user'
DATABASE_PASSWORD = 'secret'

# Make this false after your first sync, it prevents a circular dependency.
INITIAL_SYNC = True

# use development media server
SERVE_MEDIA = True

from bme.apps.brc.util import logs

LOGFILE = '/tmp/bme.log'
_loglevels = {'root' : logs.DEBUG, 'keyedcache' : logs.INFO}

log = logs.getLogger('settings', level=_loglevels,
    format="%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s",
    outfile=LOGFILE, rotation_count=10, rotation_max=4, streaming=True)
log.info("BME Started")

