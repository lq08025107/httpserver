import httplib2
from datetime import datetime
import simplejson


TESTDATA = {'woggle': {'version': 1234,
                       'updated': str(datetime.now()),
                       }}
URL = 'http://localhost:8080/form'
xmldata = """<?xml version="1.0"?>
<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>"""
jsondata = simplejson.dumps(TESTDATA)
h = httplib2.Http()
resp, content = h.request(URL,
                          'POST',
                          xmldata,
                          headers={'Content-Type': 'text/xml'})
print resp
print content