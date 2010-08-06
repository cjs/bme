import os,sys,csv, codecs, cStringIO

sys.path.append('../../../../pinax/apps')
sys.path.append('../../../../../src')
sys.path.append('../../../../../src/bme/apps')

os.environ['DJANGO_SETTINGS_MODULE'] ='bme.settings'

from bme.apps.brc.models import *

curr_year='2009'
xyear = Year.objects.filter(year=curr_year)

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

reader = UnicodeReader(open("BMEarth2009_Placement.csv", "rb"))
count = 0
for row in reader:
	try:
		tc = ThemeCamp.objects.get(bm_fm_id=row[0])
		tc.name = row[2]
		tc.description = row[3]
		tc.location_string = row[4]
		tc.save()
		print tc
	except:
		print sys.exc_info()
