# Demo 05: 爬論壇詳細資訊 (1)

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
    articleUrl="https://www.ptt.cc"+item.a["href"]
    
    articleReq=request.Request(url=articleUrl, headers=headers)
    articleRes=request.urlopen(articleReq)
    articleSoup=BeautifulSoup(articleRes, "html.parser")

    # 作者 (標題) 及時間包覆於同標籤，可以列表取項
    articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
    articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
    articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]


### Part-B
from urllib import request
from bs4 import BeautifulSoup
headers={"Cookie":"***", "User-Agent":"***"}

url="https://www.ptt.cc/bbs/Japan_Travel/index.html"
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

    articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
    articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
    articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

    good=len(articleSoup.findAll("span", {"class":"hl push-tag"}))
    # 推、噓分篇統計，要寫迴圈內 (新篇歸零)
    bad=0
    reply=articleSoup.findAll("span", {"class":"f1 hl push-tag"})
    for pushtag in reply:
        # pushtag 仍是含標籤之項，要取字串
        if pushtag.text=="噓 ":
            bad+=1


### Part-C
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

        articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
        articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
        articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

        good=len(articleSoup.findAll("span", {"class":"hl push-tag"}))
        bad=0
        reply=articleSoup.findAll("span", {"class":"f1 hl push-tag"})
        for pushtag in reply:
            if pushtag.text=="噓 ":
                bad+=1

    # 尋找上、下頁按鈕之標籤
    button=soup.findAll("a", {"class":"btn wide"})
    # 列表中取項覆寫，成為新 url
    url="https://www.ptt.cc/"+button[1]["href"]


### Part-D
from urllib import request
from bs4 import BeautifulSoup

# 引入 pandas 框架，定義表格欄位
import pandas
article=pandas.DataFrame(columns=["網址", "標題", "作者", "時間", "推數", "噓數"])
loc=0
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

        articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
        articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
        articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

        good=len(articleSoup.findAll("span", {"class":"hl push-tag"}))
        bad=0
        reply=articleSoup.findAll("span", {"class":"f1 hl push-tag"})
        for pushtag in reply:
            if pushtag.text=="噓 ":
                bad+=1

        # 依欄位逐筆增寫入列表，迴圈初始需清空
        content=[]
        content.append(articleUrl)
        content.append(articleTitle)
        content.append(articleAuthor)
        content.append(articleTime)
        content.append(good)
        content.append(bad)
        # 列表 row-index 寫入 pandas
        article.loc[loc]=content
        loc+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]
    
print(article) 


### Part-E
from urllib import request
from bs4 import BeautifulSoup

import pandas
import xlwt
import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}
article=pandas.DataFrame(columns=["網址", "標題", "作者", "時間", "推數", "噓數"])
loc=0

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

        articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
        articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
        articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

        good=len(articleSoup.findAll("span", {"class":"hl push-tag"}))
        bad=0
        reply=articleSoup.findAll("span", {"class":"f1 hl push-tag"})
        for pushtag in reply:
            if pushtag.text=="噓 ":
                bad+=1

        content=[]
        content.append(articleUrl)
        content.append(articleTitle)
        content.append(articleAuthor)
        content.append(articleTime)
        content.append(good)
        content.append(bad)
        article.loc[loc]=content
        loc+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]
    
# 將 pandas 框架轉儲為 xls 檔輸出
article.to_excel("%s/%s.xls"%(div, filename), encoding="utf-8")


### Part-F
from urllib import request
from bs4 import BeautifulSoup

import pandas
import xlwt
import os
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"Cookie":"***", "User-Agent":"***"}
article=pandas.DataFrame(columns=["網址", "標題", "作者", "時間", "推數", "噓數"])
loc=0

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

            articleAuthor=articleSoup.findAll("span", {"class":"article-meta-value"})[0].text
            articleTime=articleSoup.findAll("span", {"class":"article-meta-value"})[3].text
            articleText=articleSoup.find("div", {"id":"main-content"}).text.split("--")[0]

            good=len(articleSoup.findAll("span", {"class":"hl push-tag"}))
            bad=0
            reply=articleSoup.findAll("span", {"class":"f1 hl push-tag"})
            for pushtag in reply:
                if pushtag.text=="噓 ":
                    bad+=1

            content=[]
            content.append(articleUrl)
            content.append(articleTitle)
            content.append(articleAuthor)
            content.append(articleTime)
            content.append(good)
            content.append(bad)
            article.loc[loc]=content
            loc+=1
        # 當 title=none (如文章被刪除) 則 raise AttributeError
        except AttributeError:
            error+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
article.to_excel("%s/%s.xls"%(dir, filename), encoding="utf-8")
