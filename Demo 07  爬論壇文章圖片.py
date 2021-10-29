# Demo 07: 爬論壇文章圖片

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
    # 查找 <a> 連結，輸出為列表再篩選
    link=articleSoup.findAll("a", {"rel":"nofollow"})

 
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
        link=articleSoup.findAll("a", {"rel":"nofollow"})

    # 尋找上、下頁按鈕之標籤
    button=soup.findAll("a", {"class":"btn wide"})
    # 列表中取項覆寫，成為新 url
    url="https://www.ptt.cc/"+button[1]["href"]


### Part-C
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
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
        link=articleSoup.findAll("a", {"rel":"nofollow"})
        
        # 篩選列表項 (imgur表圖片) 並下載
        for image in link:
            if "imgur" in image["href"]:
                location=dir+"/%d.jpg"%(imageId)
                request.urlretrieve(image["href"], location)

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]


### Part-D
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
# 累積報錯數，供結果輸出
error=articleId=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        # 有兩處可能報錯 (文章遭刪除、網址斷行)
        try:
            # 分篇統計下載圖片數量，供結果輸出
            imageId=0
            articleId+=1
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]
    
            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            link=articleSoup.findAll("a", {"rel":"nofollow"})
            
            for image in link:
                try:
                    if "imgur" in image["href"]:
                        imageId+=1
                        # 標題常包含不可存檔之字元，以 id 代之
                        location=dir+"/%d_%d.jpg"%(articleId, imageId)
                        request.urlretrieve(image["href"], location)
                except:
                    error+=1
            print("已下載第 %d 篇文章，共 %d 張圖片"%(articleId, imageId))
        except:
            error+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，出現 %d 個下載錯誤"%(error))


### Demo 7-1: #PTT 日本旅遊版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
pages=int(input("欲爬取頁面數量："))
error=articleId=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"title"})
    for item in target:
        try:
            imageId=0
            articleId+=1
            articleTitle=item.a.text
            articleUrl="https://www.ptt.cc"+item.a["href"]
    
            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            link=articleSoup.findAll("a", {"rel":"nofollow"})
            
            for image in link:
                try:
                    if "imgur" in image["href"]:
                        imageId+=1
                        location=dir+"/%d_%d.jpg"%(articleId, imageId)
                        request.urlretrieve(image["href"], location)
                except:
                    error+=1
            print("已下載第 %d 篇文章，共 %d 張圖片"%(articleId, imageId))
        except:
            error+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，出現 %d 個下載錯誤"%(error))


### Demo 7-2: #BabyHome 美味料理版
from urllib import request
from bs4 import BeautifulSoup

import os
dir=input("輸入檔案路徑：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}

url="https://forum.babyhome.com.tw/list/1035"
pages=int(input("欲爬取頁面數量："))
error=articleId=0
for i in range(pages):
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    target=soup.findAll("div", {"class":"forum_l2_list_main"})
    for item in target:
        try:
            imageId=0
            articleId+=1
            articleTitle=item.a.text
            articleUrl=item.a["href"]
    
            articleReq=request.Request(url=articleUrl, headers=headers)
            articleRes=request.urlopen(articleReq)
            articleSoup=BeautifulSoup(articleRes, "html.parser")
            content=articleSoup.find("div", {"class":"threads_body"}).findAll("img")
            
            for image in content:
                try:
                    if "jpg" in image["src"]:
                        imageId+=1
                        location=dir+"/%d_%d.jpg"%(articleId, imageId)
                        request.urlretrieve(image["src"], location)
                except:
                    error+=1
            print("已下載第 %d 篇文章，共 %d 張圖片"%(articleId, imageId))
        except:
            error+=1

    button=soup.find("li", {"class":"next"})
    url=button.a["href"]

print("爬蟲結束，出現 %d 個下載錯誤"%(error))
