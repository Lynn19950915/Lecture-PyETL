<h2 align="center">Appendix B: RSS 爬蟲</h2>

- Sample B1
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://about.pts.org.tw/rss/XML/newsletter.xml"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)

# 以 lxml 處理 xml 網頁，如同 html.parser 處理一般網頁
soup=BeautifulSoup(res, "lxml")
print(soup)
```
<br/>

- Sample B2: #公視新聞稿
```
from urllib import request
from bs4 import BeautifulSoup

# pandas 框架搭配 xls 檔案輸出
import pandas
import xlwt
article=pandas.DataFrame(columns=["標題", "文章內容"])
loc=0
headers={"User-Agent":"***"}
url="https://about.pts.org.tw/rss/XML/newsletter.xml"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "lxml")

target=soup.findAll("item")
for item in target:
    articleTitle=item.title.text
    articleText=item.description.text

    content=[]
    content.append(articleTitle)
    content.append(articleText)
    # 逐筆 row-index 寫入列表中  
    article.loc[loc]=content
    loc+=1

print("爬蟲結束，共計 %d 篇文章"%(loc))
article.to_excel("C:/PyETL/公視新聞稿.xls", encoding="utf-8")
```
<br/>

- Sample B3: #BBC 中文網國際新聞版
```
from urllib import request
from bs4 import BeautifulSoup

# pandas 框架搭配 xls 檔案輸出
import pandas
import xlwt
article=pandas.DataFrame(columns=["網址", "標題", "時間", "文章內容"])
loc=0
headers={"User-Agent":"***"}
url="http://www.bbc.co.uk/zhongwen/trad/world/index.xml"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "lxml")

target=soup.findAll("entry")
for item in target:
    articleUrl=item.link["href"]
    articleTitle=item.title.text
    articleTime=item.published.text
    articleText=item.summary.text

    content=[]
    content.append(articleUrl)
    content.append(articleTitle)
    content.append(articleTime)
    content.append(articleText)
    # 逐筆 row-index 寫入列表中
    article.loc[loc]=content
    loc+=1

print("爬蟲結束，共計 %d 篇文章"%(loc))
article.to_excel("C:/PyETL/BBC中文網國際新聞版.xls", encoding="utf-8")
```
