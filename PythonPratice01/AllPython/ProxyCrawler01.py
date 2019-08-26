# -*- coding: utf-8 -*-
import urllib.request
import re
import sys
import datetime
import time
import random

#reload(sys)
#sys.setdefaultencoding('utf8')


url_headers={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
             "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
             "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
             "cookie":"__cfduid=d2d1fb2a4d258e653576861a70a3ee27e1545371736; cf_clearance=572e3ab56e6034beb68329f13785b3a04cdc368f-1545371740-86400-150; t=89505992; _ga=GA1.2.1238139149.1545371729; _gid=GA1.2.578381551.1545371729; _ym_uid=1545371729456011672; _ym_d=1545371729; _fbp=fb.1.1545371729289.2031468140; _ym_visorc_42065329=w; _ym_isad=2; jv_enter_ts_EBSrukxUuA=1545371730967; jv_visits_count_EBSrukxUuA=1; jv_refer_EBSrukxUuA=https%3A%2F%2Fhidemyna.me%2Fen%2Fproxy-list%2F%3Fcountry%3DAFALDZADAOARAMAUATAZBDBYBEBJBOBABWBRBGBFKHCMCACVCLCNCOCRCIHRCYCZDKDJDOECEGSVGQEEFIFRGAGEDEGHGRGTHTHNHKHUINIDIRIQIEIMILITJMJPJEKZKEKRKWKGLVLBLSLRLYLTLUMKMGMWMYMVMTMUMXMDMNMEMZMMNPNLNZNINGNOPKPSPAPGPYPEPHPLPTPRRORURWWSRSSCSGSKSISOZASSESSECHTWTJTZTHTRUGUAGBUSVEVNVIZMZW; jv_utm_EBSrukxUuA=; analytic_id=1545371730976; _dc_gtm_UA-90263203-1=1; _gat_UA-90263203-1=1; jv_pages_count_EBSrukxUuA=2",
             }


urltw="https://hidemyna.me/en/proxy-list/?country=TW#list"
url="https://hidemyna.me/en/proxy-list/?country=AFALDZADAOARAMAUATAZBDBYBEBJBOBABWBRBGBFKHCMCACVCLCNCOCRCIHRCYCZDKDJDOECEGSVGQEEFIFRGAGEDEGHGRGTHTHNHKHUINIDIRIQIEIMILITJMJPJEKZKEKRKWKGLVLBLSLRLYLTLUMKMGMWMYMVMTMUMXMDMNMEMZMMNPNLNZNINGNOPKPSPAPGPYPEPHPLPTPRRORURWWSRSSCSGSKSISOZASSESSECHTWTJTZTHTRUGUAGBUSVEVNVIZMZW&start="

ipn=64
page=0
num=0
slti=5

inpage=0
while inpage<=0:
    inpage=int(input("Input crawler page number: "))
    if inpage<=0:
        print("input wrong pages!!Please input again!!")
        continue


#today=datetime.date.today()
today=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime()) 
starttime=time.time()
print("\nStart Crawler!!\n")
while page<inpage:

    time.sleep(random.randint(1,slti))
    upage=str(num)
    fullurl=url+upage
    req=urllib.request.Request(fullurl,headers=url_headers)
    repsonse = urllib.request.urlopen(req)

    pattern=re.compile("""(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d{1,5})</td><td><div><span class="flag-icon flag-icon-[a-zA-Z]{1,5}"></span> &nbsp;([a-zA-Z\-\s ]*)\s?<span>[&quot; ]*([a-zA-Z\s\- ]*)?""")

    items=re.findall(pattern,repsonse.read().decode("ISO-8859-1"))

    
    with open ("proxy"+str(today)+".txt","a") as pt:
        for it in items:
            pt.write(it[0]+":"+it[1]+" "+it[2]+" "+it[3]+" \n")
            
    print("page:",page+1," Finish!!")

    page+=1
    num=page*ipn
    
    
pt.close()
endtime=time.time()
usetime=endtime-starttime
print("\nCrawler Finish!!\n")
print("use time:"+str(round(usetime,1))+"s")
        
#print(type(repsonse.read().decode("ISO-8859-1")))
#print(repsonse.read().decode("ISO-8859-1"))
