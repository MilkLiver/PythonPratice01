import requests
import re
import json
import urllib
from urllib.parse import urlparse
import shutil

res = requests.get('https://www.youtube.com/watch?v=OVuYIMa5XBw')
print(type(res.text))
print(res.text)

m = re.search('layer.config = ({.*?});',res.text)
print(m.group(1))

jd = json.loads(m.group(1))
print(jd["args"]["adaptive_fmts"])

parsed = urlparse(jd["args"]["adaptive_fmts"])
a = urllib.parse.parse_qs(jd["args"]["adaptive_fmts"])
print(a['url'][0])

res2 = requests.get(a['url'][0], stream = True)
f = open('b.mp4', 'wb')
shutil.copyfileobj(res2.raw, f)
f.close()
