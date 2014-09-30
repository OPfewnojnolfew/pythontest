"""bugrequests"""
import requests
import re

#


class BugMine:

    """BugMine"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'\
        '(KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36'}
    #----------------------------------------------------------------------

    def __init__(self, param):
        self.login_url = param['login_url']
        self.login_params = param['login_params']
        self.bug_url = param['bug_url']
        self.request_hander = requests.session()
        self.login()

    def login(self):
        """login"""
        self.request_hander.post(
            self.login_url, self.login_params, headers=BugMine.headers)

    def mybug(self):
        """mybug"""
        req = self.request_hander.get(self.bug_url, headers=BugMine.headers)
        req.encoding = 'utf-8'
        myitems = re.findall(r"<td\s+class='a-left\s+nobr'>[\s\n]*?"\
            r"<a\s+href='(.*?)'\s*>[\s\S]*?</a>[\s\n]*?"\
            "</td>", req.text, re.S)
        print(myitems)
        for item in myitems:
            self.mybug_detail(item)

    def mybug_detail(self, url):
        """mybug_detail"""
        req = self.request_hander.get(
            'http://192.168.60.251' + url, headers=BugMine.headers)
        req.encoding = 'utf-8'
        detail_title = re.findall(r"<div\s+id='titlebar'\s*>[\s\n]*?"\
            r"<div\s+id='main'\s*>([\s\S]*?)</div>", req.text, re.S)
        detail_content = re.findall(r"<div\s+class='content'\s*>([\s\S]*?)"\
            "</div>", req.text, re.S)
        print(detail_title)
        for item in detail_content:
            print(item.replace('<[^>]*>', ''))
# pylint: disable=C0103
bug_mine = BugMine({
    'login_url': '''http://192.168.60.251/zentaopms/www/index.php
                ?m=user&f=login''',
    'bug_url': '''http://192.168.60.251/zentaopms/www/index.php
                ?m=my&f=bug&type=assignedTo''',
    'login_params': {'account': 'pangtengfei',
                     'password': '123456',
                     'referer': ''}
})
bug_mine.mybug()
