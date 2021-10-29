<h2 align="center">Lesson 04: 圖片查取及下載</h2>

- Sample 15
```
from urllib import request
from bs4 import BeautifulSoup
# headers, Cookies 為字典格式，寫在同一本
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/M.1575204621.A.A95.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 查找 <a> 聯結，輸出為列表再篩選
link=soup.findAll("a", {"rel":"nofollow"})
for item in link:
    # 篩選包含 imgur (圖片) 者縮排輸出
    if "https://i.imgur.com" in item["href"]:
        print("\t"+item.text)
```
<br/>

- Sample 16: re模組：re.search()
```
from urllib import request
from bs4 import BeautifulSoup
import re
# headers, Cookies 為字典格式，寫在同一本
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/M.1575204621.A.A95.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 查找 <a> 聯結，輸出為列表再篩選
link=soup.findAll("a", {"rel":"nofollow"})
for item in link:
    # search 於字串中搜尋，group 輸出完整字串
    match=re.search(r"https://i.imgur[a-zA-Z0-9/._]+", item["href"])
    if match:
        print(match.group())
```
<br/>

- Sample 17: re模組：re.findall()
```
from urllib import request
from bs4 import BeautifulSoup
import re
# headers, Cookies 為字典格式，寫在同一本
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/M.1575204621.A.A95.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 查找 <a> 聯結，輸出為列表再篩選
link=soup.findAll("a", {"rel":"nofollow"})
for item in link:
    # findall (注意：非 findAll) 以列表輸出結果，取首項即可
    match=re.findall(r"https://i.imgur[a-zA-Z0-9/._]+", item["href"])
    if match:
        print(match[0])
```
<br/>

- Sample 18: urlretrieve
```
from urllib import request
from bs4 import BeautifulSoup
# headers, Cookies 為字典格式，寫在同一本
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Japan_Travel/M.1575204621.A.A95.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

title=soup.findAll("span", {"class":"article-meta-value"})[2].text
# 查找 <a> 聯結，輸出為列表再篩選
link=soup.findAll("a", {"rel":"nofollow"})
# enumerate 產生數對 (逐項遞增)
for n, item in enumerate(link):
    # 篩選包含 imgur (圖片) 者縮排輸出
    if "https://i.imgur.com" in item["href"]:
        location="C:/PyETL/%s_%d.jpg"%(title, n)
        # 下載 url 於指定本地位址
        request.urlretrieve(item["href"], location)
```
