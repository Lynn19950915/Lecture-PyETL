# Demo 01: 爬論壇單頁標題

### Part-A
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")
# 以 prettify 查探排版之網頁結構
print(soup.prettify())


### Part-B
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")
# 標題包覆於 title 標籤中，findAll 可爬取多項物件清單
target=soup.findAll("div", {"class":"title"})
print(target)


### Part-C
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

target=soup.findAll("div", {"class":"title"})
# 以迴圈取出清單中物件，並往內層 <a> 爬取內容字串
for item in target:
    articleTitle=item.a.text
    # 應用 <a> 標籤屬性，組合輸出文章 url
    articleUrl="https://www.ptt.cc"+item.a["href"]


### Part-D
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

target=soup.findAll("div", {"class":"title"})
for item in target:
    articleTitle=item.a.text
    articleUrl="https://www.ptt.cc"+item.a["href"]

    # 開檔 (a-mode) 附加寫入
    file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
    file.write(articleTitle+"\n"+articleUrl+"\n")
    file.close()


### Part-E
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

error=0
target=soup.findAll("div", {"class":"title"})
for item in target:
    try:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]

        file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
        file.write(articleTitle+"\n"+articleUrl+"\n")
        file.close()
    # 當 title=none (如文章被刪除) 則 raise AttributeError
    except AttributeError:
        # 不寫入內容，累積一個錯誤
        error+=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 1-1: #PTT 日本旅遊版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

error=0
target=soup.findAll("div", {"class":"title"})
for item in target:
    try:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]

        file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
        file.write(articleTitle+"\n"+articleUrl+"\n")
        file.close()
    except AttributeError:
        error+=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 1-2: #BabyHome 美味料理版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://forum.babyhome.com.tw/list/1035"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

error=0
target=soup.findAll("div", {"class":"forum_l2_list_main"})
for item in target:
    try:
        articleTitle=item.a.text
        articleUrl=item.a["href"]

        file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
        file.write(articleTitle+"\n"+articleUrl+"\n")
        file.close()
    except AttributeError:
        error+=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
