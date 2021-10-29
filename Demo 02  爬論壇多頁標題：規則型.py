# Demo 02: 爬論壇多頁標題：規則型

### Part-A
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}

index=7055
pages=int(input("欲爬取頁面數量："))
while index>7055-pages:
    # 可變網址以格式化字符取代，寫於迴圈內
    url="https://www.ptt.cc/bbs/Japan_Travel/index%d.html"%(index)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]
    index-=1


### Part-B
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

index=7055
pages=int(input("欲爬取頁面數量："))
while index>7055-pages:
    url="https://www.ptt.cc/bbs/Japan_Travel/index%d.html"%(index)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]

        # 開檔 (a-mode) 附加寫入
        file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
        file.write(articleTitle+"\n"+articleUrl+"\n")
        file.close()
    index-=1


### Part-C
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

index=7055
pages=int(input("欲爬取頁面數量："))
# 累積報錯數，供結果輸出
error=0
while index>7055-pages:
    url="https://www.ptt.cc/bbs/Japan_Travel/index%d.html"%(index)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]

            file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n")
            file.close()        
        # 當 title=none (如文章被刪除) 則 raise AttributeError
        except AttributeError:
            error+=1
    index-=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 2-1: #PTT 日本旅遊版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

index=7055
pages=int(input("欲爬取頁面數量："))
error=0
while index>7055-pages:
    url="https://www.ptt.cc/bbs/Japan_Travel/index%d.html"%(index)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]

            file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n")
            file.close()       
        except AttributeError:
            error+=1
    index-=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 2-2: #BabyHome 美味料理版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

index=1
pages=int(input("欲爬取頁面數量："))
error=0
while index<pages+1:
    url="https://forum.babyhome.com.tw/list/1035?page=%d"%(index)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"forum_l2_list_main"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl=item.a["href"]

            file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n")
            file.close()       
        except AttributeError:
            error+=1
    index+=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
