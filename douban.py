import urllib.request as ur
import json
import os
import sys
os.chdir(sys.path[0])

t = r'http://douban.fm/j/mine/playlist?type=n&channel='

for i in range(24):
    url = t + str(i)
    print(url)
    a=ur.urlopen(url).read().decode().replace('\\','')
    a=json.loads(a)
    for i in a['song']:
        filename = i['artist']+'-'+i['albumtitle']+'.mp3'
        print('正在下载:','艺术家: '+i['artist'],'曲目: '+i['albumtitle'],'地址: '+i['url'],sep='\n',end='\n\n')
        try:
            if os.path.exists(filename):
                print('以存在本文件，下载下一个中')
                break
            ur.urlretrieve(i['url'],filename)
            if os.path.getsize(filename)<300:
                os.system('del '+filename)
        except Exception as a:
            print (a)
            pass
