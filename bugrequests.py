import requests
from bs4 import BeautifulSoup

########################################################################
class BugMine:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36'}
    #----------------------------------------------------------------------
    def __init__(self,param):
        self.loginUrl=param['loginUrl']
        self.loginParams=param['loginParams']
        self.bugUrl=param['bugUrl']
        self.requestHander=requests.session()
        self.login()
    def login(self):
        self.requestHander.post(self.loginUrl,self.loginParams,headers=BugMine.headers);
    def getMyBug(self):
        req=self.requestHander.get(self.bugUrl,headers=BugMine.headers)
        req.encoding = 'utf-8'
        soup=BeautifulSoup(req.text)
        print(soup.prettify())
        soupItems= soup.find_all("p", class_="a-left nobr")

        items=[]
        for item in items:
            items.append(item.get('href'))
bugMine=BugMine({
    'loginUrl':'http://192.168.60.251/zentaopms/www/index.php?m=user&f=login',
    'bugUrl':'http://192.168.60.251/zentaopms/www/index.php?m=my&f=bug&type=assignedTo',
    'loginParams':{'account':'pangtengfei','password':'123456', 'referer':''}
})
print(bugMine.getMyBug())