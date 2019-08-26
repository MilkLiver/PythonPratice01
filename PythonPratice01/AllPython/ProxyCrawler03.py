# -*- coding: utf-8 -*-
import urllib.request
import re
import sys
import datetime
import time
import random

#reload(sys)
#sys.setdefaultencoding('utf8')

def proxyCrawler():
    url_headers={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                 "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                 "cookie":"__cfduid=dae8cb1d2740e48449598880e7795467d1545623030; cf_clearance=c3cc939dd6503ed7fc6852e2a7b03116ace7ba28-1545623034-86400-150; t=90015357; _ga=GA1.2.351828463.1545623013; _gid=GA1.2.1423836486.1545623013; _ym_uid=1545623013687739595; _ym_d=1545623013; _fbp=fb.1.1545623012858.1037869963; _ym_isad=2; _ym_visorc_42065329=w; analytic_id=1545623013829; jv_enter_ts_EBSrukxUuA=1545623014216; jv_visits_count_EBSrukxUuA=1; jv_refer_EBSrukxUuA=https%3A%2F%2Fhidemyna.me%2Fen%2Fproxy-list%2F; jv_utm_EBSrukxUuA=; _dc_gtm_UA-90263203-1=1; _gat_UA-90263203-1=1; jv_pages_count_EBSrukxUuA=2",
                 }
    
    
    urltw="https://hidemyna.me/en/proxy-list/?country=TW#list"
    url="https://hidemyna.me/en/proxy-list/?country=AFALDZADAOARAMAUATAZBDBYBEBJBOBABWBRBGBFKHCMCACVCLCNCOCRCIHRCYCZDKDJDOECEGSVGQEEFIFRGAGEDEGHGRGTHTHNHKHUINIDIRIQIEIMILITJMJPJEKZKEKRKWKGLVLBLSLRLYLTLUMKMGMWMYMVMTMUMXMDMNMEMZMMNPNLNZNINGNOPKPSPAPGPYPEPHPLPTPRRORURWWSRSSCSGSKSISOZASSESSECHTWTJTZTHTRUGUAGBUSVEVNVIZMZW&start="
    
    ipn=64
    page=0
    num=0
    slti=5
    
    inpage=0

    while True:
        filename=input("Input save file name or (default): ")
        if filename:
            break
        print("you don't input anything!! \n")
    
    
    while inpage<=0:
        print("\n")
        inpage=int(input("Input crawler page number: "))
        if inpage<=0:
            print("input wrong pages!!Please input again!!")
            continue
    
    
    #today=datetime.date.today()
    today=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime()) 
    starttime=time.time()
    print("\nStart Crawler!!\n")

    deputypattern=re.compile("""(\.txt)$""")
    deputyname=re.findall(deputypattern,filename)

    if filename=="default":
        filename="proxy"+str(today)+".txt"
    
    if not deputyname:
        filename=filename+".txt"
    
    while page<inpage:
    
        time.sleep(random.randint(1,slti))
        upage=str(num)
        fullurl=url+upage
        req=urllib.request.Request(fullurl,headers=url_headers)
        repsonse = urllib.request.urlopen(req)
    
        pattern=re.compile("""(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d{1,5})</td><td><div><span class="flag-icon flag-icon-[a-zA-Z]{1,5}"></span> &nbsp;([a-zA-Z- ]*)<span>[&quot; ]*([a-zA-Z-' ]*)[&quot;]*\s?</span></div></td><td><div class=bar><div class=n-bar-wrapper style="background-position:\-?\d{1,5}[px]{0,2} \-?\d{1,5}[px]{0,2}"><p>(\d{1,6}) ms</p><div class=n-bar-speed><em style="width:\d{1,5}[px]{0,2};background:#[\w]{1,6}\;?\}?"></em></div></div></div></td><td>([a-zA-Z0-9]*)""")
    
        items=re.findall(pattern,repsonse.read().decode("ISO-8859-1"))

        with open (filename,"a") as pt:
            for it in items:
                pt.write(it[0]+":"+it[1]+" "+it[2]+" "+it[3]+" "+it[4]+" "+it[5]+" \n")
                
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

def readProxyFile():
    while True:
        filename=input("Input load file name: ")
        if filename:
            break
        print("you don't input anything!! \n")

    deputypattern=re.compile("""(\.txt)$""")
    deputyname=re.findall(deputypattern,filename)

    if filename=="default":
        filename="proxy"+str(today)+".txt"
    
    elif not deputyname:
        filename=filename+".txt"

    while True:
        print("\ninput what you want to search:")
        print("\n1. Search all")
        print("\n2. Search specific country")
        print("\n3. Search specific porxy type\n")
    
        method=input("method: ")
        print("\n")

        if not method:
            print("\nyou don't input anything!! \n")
    
        if method=="1":
            searpattern=""".*"""
            break
        
        elif method=="2":
            searchpurpose=input("input what country you want to search: ")
            if not searchpurpose:
                print("\nyou don't input anything!! \n")
                continue
            searpattern=re.compile(searchpurpose)
            break

        elif method=="3":
            print("input what porxy type you want to search: \n")
            print("\n1. HTTP\n2. HTTPS\n3. SOCKS 4\n4. SOCKS 5")
            searchpurpose=str(input("proxy type: "))
            print(searchpurpose)

            if not searchpurpose:
                print("\nyou don't input anything!! \n")
                continue
            elif searchpurpose !="1" and searchpurpose!="2" and searchpurpose!="3" and searchpurpose!="4" and searchpurpose!="HTTP" and searchpurpose!="HTTPS" and searchpurpose!="SOCKS4" and searchpurpose!="SOCKS5" and searchpurpose!="SOCKS 4" and searchpurpose!="SOCKS 5":
                print("\nNo this proxy type!!\n")
                continue
            if searchpurpose=="1" or searchpurpose=="HTTP":
                searchpurpose="HTTP"
            elif searchpurpose=="2" or searchpurpose=="HTTPS":
                searchpurpose="HTTPS"
            elif searchpurpose=="3" or searchpurpose=="SOCKS4" or searchpurpose=="SOCKS 4":
                searchpurpose="SOCKS4"
            elif searchpurpose=="4" or searchpurpose=="SOCKS5" or searchpurpose=="SOCKS 5":
                searchpurpose="SOCKS5"
            searpattern=re.compile(searchpurpose)
            break

        else:
            print("No method Please input again!!\n")
    try:
        with open (filename,"r") as rf:
            for it in rf.readlines():
                reit=re.findall(searpattern,it)
                if reit:
                    print(it,end="")
        rf.close()
    except FileNotFoundError:
        print("No such file or %s"%(filename))


if __name__=="__main__":
    while True:
        print("\ninput the method:\n1. read\n2. crawl\n3. exit\n")
        operate=input("method: ")
        print("\n")
        if operate=="read" or operate=="1":
            readProxyFile()
        elif operate=="crawl"or operate=="2":
            proxyCrawler()
        elif operate=="exit"or operate=="3":
            break
        else:
            print("No method please input again!")
