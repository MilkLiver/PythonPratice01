import http.cookiejar
import urllib.request
import urllib.parse



if __name__=="__main__":

    url_headers={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                 "accept-language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                 "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                 "cookie":"__cfduid=dae8cb1d2740e48449598880e7795467d1545623030; cf_clearance=c3cc939dd6503ed7fc6852e2a7b03116ace7ba28-1545623034-86400-150; t=90015357; _ga=GA1.2.351828463.1545623013; _gid=GA1.2.1423836486.1545623013; _ym_uid=1545623013687739595; _ym_d=1545623013; _fbp=fb.1.1545623012858.1037869963; _ym_isad=2; _ym_visorc_42065329=w; analytic_id=1545623013829; jv_enter_ts_EBSrukxUuA=1545623014216; jv_visits_count_EBSrukxUuA=1; jv_refer_EBSrukxUuA=https%3A%2F%2Fhidemyna.me%2Fen%2Fproxy-list%2F; jv_utm_EBSrukxUuA=; _dc_gtm_UA-90263203-1=1; _gat_UA-90263203-1=1; jv_pages_count_EBSrukxUuA=2",
                 }
    #headers_key=list(url_headers)
    #headers_list=[]
    #for i in headers_key:
    #    headers_list.append(i)
    #    headers_list.append(url_headers[i])
    #headers_tuple=tuple(headers_list)
    #print(type(headers_set))
    #print(headers_set)
    

    #cookie_str="__cfduid=dae8cb1d2740e48449598880e7795467d1545623030; cf_clearance=c3cc939dd6503ed7fc6852e2a7b03116ace7ba28-1545623034-86400-150; t=90015357; _ga=GA1.2.351828463.1545623013; _gid=GA1.2.1423836486.1545623013; _ym_uid=1545623013687739595; _ym_d=1545623013; _fbp=fb.1.1545623012858.1037869963; _ym_isad=2; _ym_visorc_42065329=w; analytic_id=1545623013829; jv_enter_ts_EBSrukxUuA=1545623014216; jv_visits_count_EBSrukxUuA=1; jv_refer_EBSrukxUuA=https%3A%2F%2Fhidemyna.me%2Fen%2Fproxy-list%2F; jv_utm_EBSrukxUuA=; _dc_gtm_UA-90263203-1=1; _gat_UA-90263203-1=1; jv_pages_count_EBSrukxUuA=2"
    
    url="https://hidemyna.me/en/proxy-list"
    
    cj=http.cookiejar.CookieJar()
    
    handler=urllib.request.HTTPCookieProcessor(cj)
    
    opener=urllib.request.build_opener(handler)

    #opener.addheaders=[headers_tuple]
    
    #response = opener.open(url,headers=url_headers)
    
    #try:
    #    response = opener.open(url,headers=url_headers)
    #except:
    #    response = opener.open(url)
    print(response.read())
    
    for items in cj:
        print(items.name)
        print(items.value)
