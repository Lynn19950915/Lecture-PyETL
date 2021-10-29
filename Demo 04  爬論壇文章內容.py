# Demo 04: 爬論壇文章內容

### Part-A
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}

# 最新頁面，無需帶數字參數
url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

target=soup.findAll("div", {"class":"title"})
for item in target:
    articleTitle=item.a.text
    # 文章內容即是以此 url，向下多爬一層而來
    articleUrl="https://www.ptt.cc"+item.a["href"]
    
    articleReq=request.Request(url=articleUrl, headers=headers)
    articleRes=request.urlopen(articleReq)
    articleSoup=BeautifulSoup(articleRes, "html.parser")


### Part-B
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
# 迴圈執行 pages 次
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]

        articleReq=request.Request(url=articleUrl, headers=headers)
        articleRes=request.urlopen(articleReq)
        articleSoup=BeautifulSoup(articleRes, "html.parser")
        # div#main-content 包含留言回覆：以分隔符切開字串
        articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

    # 尋找上、下頁按鈕之標籤
    button=soup.findAll("a", {"class":"btn wide"})
    # 列表中取項覆寫，成為新url
    url="https://www.ptt.cc/"+button[1]["href"]


### Part-C
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        articleTitle=item.a.text
        articleUrl="https://www.ptt.cc"+item.a["href"]

        articleReq=request.Request(url=articleUrl, headers=headers)
        articleRes=request.urlopen(articleReq)
        articleSoup=BeautifulSoup(articleRes, "html.parser")
        articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]
        
        # 開檔 (a-mode) 附加寫入
        file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
        file.write(articleTitle+"\n"+articleUrl+"\n"+articleText)
        file.close()

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

    
### Part-D
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
# 累積報錯數，供結果輸出
error=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]

            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]
            
            file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n"+articleText)
            file.close()
        # 當 title=none (如文章被刪除) 則 raise AttributeError
        except AttributeError:
            error+=1
      
    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 4-1: #PTT 日本旅遊版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
error=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]

            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]
            
            file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n"+articleText)
            file.close()
        except AttributeError:
            error+=1
      
    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))


### Demo 4-2: #BabyHome 美味料理版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://forum.babyhome.com.tw/list/1035"
pages=int(input("欲爬取頁面數量："))
error=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"forum_l2_list_main"})
    for item in target:
        try:
            articleTitle=item.a.text
            articleUrl=item.a["href"]

            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            articleText=articleSoup.findAll("div", {"class":"threads_content"})[0].text
            
            file=open("%s/%s.txt"%(dir, filename), "a", encoding="utf-8")
            file.write(articleTitle+"\n"+articleUrl+"\n"+articleText)
            file.close()
        except AttributeError:
            error+=1
      
    button=soup.find("li", {"class":"next"})
    url=button.a["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
