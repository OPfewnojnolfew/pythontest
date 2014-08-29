import urllib.request
import urllib.parse
import http.cookiejar
import re

########################################################################
class BugMine:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36'}
    #----------------------------------------------------------------------
    def __init__(self,param):
        self.loginUrl=param['loginUrl']
        self.loginParams=param['loginParams']
        self.bugUrl=param['bugUrl']
        cookie=http.cookiejar.CookieJar()
        processor=urllib.request.HTTPCookieProcessor(cookie)
        self.opener=urllib.request.build_opener(processor)   
    def login(self):
        loginreq = urllib.request.Request(self.loginUrl, urllib.parse.urlencode(self.loginParams).encode('utf-8'),headers=BugMine.headers)  
        self.opener.open(loginreq)
    def getMyBug(self):
        self.login()
        bugPage=self.opener.open(self.bugUrl).read().decode("utf-8")
        print(bugPage)
        myItems = re.findall("<td\s+class='a-left\s+nobr'><a\s+href='(.*)'\s*>[\s\S]*</a></td>",bugPage,re.S)    
        items=[]
        for item in myItems:
            items.append(item)
bugMine=BugMine({
    'loginUrl':'http://192.168.60.251/zentaopms/www/index.php?m=user&f=login',
    'bugUrl':'http://192.168.60.251/zentaopms/www/index.php?m=my&f=bug&type=assignedTo',
    'loginParams':{'account':'pangtengfei','password':'123456', 'referer':''}
})
print(bugMine.getMyBug())