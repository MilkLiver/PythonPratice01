import requests
import re
import json
import urllib
from urllib.parse import urlparse
import shutil

res = requests.get('https://www.youtube.com/watch?v=OVuYIMa5XBw')
print(type(res.text))
#print(res.text)

print("\n")
m = re.findall('layer.config = ({.*?});',res.text)
print(len(m))
print(m[0])

jd = json.loads(m[0])
print(jd)
#print(jd["args"]["adaptive_fmts"])

parsed = urlparse(jd["args"]["adaptive_fmts"])
#print(parsed)
a = urllib.parse.parse_qs(jd["args"]["adaptive_fmts"])

print("\n")
#print(a['url'][1])

res2 = requests.get(a['url'][0], stream = True)
print(res2.raw)
#f = open('a.mp4', 'wb')
#shutil.copyfileobj(res2.raw, f)
#f.close()
