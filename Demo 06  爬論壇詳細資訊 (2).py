# Demo 06: 爬論壇詳細資訊 (2)

### Demo 6-1: #PTT 日本旅遊版
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
        except AttributeError:
            error+=1

    button=soup.findAll("a", {"class":"btn wide"})
    url="https://www.ptt.cc/"+button[1]["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
article.to_excel("%s/%s.xls"%(dir, filename), encoding="utf-8")


### Demo 6-2: #BabyHome 美味料理版
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
article=pandas.DataFrame(columns=["網址", "標題", "作者", "時間", "最新回覆"])
loc=0

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

            articleAuthor=articleSoup.find("a", {"class":"author_name"}).text
            articleTime=articleSoup.find("span", {"class":"threads_time"}).text
            articleText=articleSoup.findAll("div", {"class":"threads_content"})[0].text
            newestReply=articleSoup.findAll("div", {"class":"threads_content"})[-1].text

            content=[]
            content.append(articleUrl)
            content.append(articleTitle)
            content.append(articleAuthor)
            content.append(articleTime)
            content.append(newestReply)
            article.loc[loc]=content
            loc+=1
        except AttributeError:
            error+=1

    button=soup.find("li", {"class":"next"})
    url=button.a["href"]

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
article.to_excel("%s/%s.xls"%(dir, filename), encoding="utf-8")
