import urllib.parse
import urllib.request
import re




ua_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
url="http://www.baidu.com/s?"
keyword=input("請輸入你要搜索的訊息: ")
wd={"wd":keyword}
#wd=("wd",keyword)
#wd=urllib.parse.urlencode(wd)
wd = urllib.parse.urlencode(wd)
fullUrl=url+wd
print(fullUrl)

req=urllib.request.Request(fullUrl,headers=ua_headers)
response=urllib.request.urlopen(req)

# with open("baiduSearch.html","wb") as f:
#     f.write(response.read())

pattern=re.compile("""<a target="_blank" href='([\s\S]*?)'>([\s\S]*?)</a>""")
items=re.findall(pattern,response.read().decode('utf-8'))
for it in items:
    print(it[0],it[1])
