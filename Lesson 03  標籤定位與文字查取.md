<h2 align="center">Lesson 03: 標籤定位與文字查取</h2>

- Sample 09: "標籤", 屬性="值"
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# 前者僅印出首項、後者以清單型態展列，有保留字問題
target1=soup.find("div", id="main-container")
print(target1)
target2=soup.findAll("div", id="main-container")
print(target2)
```
<br/>

- Sample 10: "標籤", {"屬性":"值"}
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# 前者僅印出首項、後者以清單型態展列，無保留字問題
target3=soup.find("div", {"id":"main-container"})
print(target3)
target4=soup.findAll("div", {"id":"main-container"})
print(target4)
```
<br/>

- Sample 11: "標籤\[屬性='值']"
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# 前者僅印出首項、後者以清單型態展列，有保留字問題
target5=soup.select_one("div[id='action-bar-container']")
print(target5)
target6=soup.select("div[id='action-bar-container']")
print(target6)
```
<br/>

- Sample 12: 標籤子查詢
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# find 已是單值物件，直接 .div 即可取出內層標籤
target1=soup.find("div", id="main-container")
subque1=target1.div
print(subque1)

# findAll 為清單，需取出首項物件方可進取內層標籤
target2=soup.findAll("div", id="main-container")
subque2=target2[0].a
print(subque2)
```
<br/>

- Sample 13: 內容子查詢
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# find 已是單值物件，直接 .div 即可取出內層標籤
target1=soup.find("div", id="main-container")
# 以 .text 取出 (注意：同層) 內容
subque3=target1.div.text
print(subque3)

# findAll 為清單，需取出首項物件方可進取內層標籤
target2=soup.findAll("div", id="main-container")
# 以 .text 取出 (注意：同層) 內容
subque4=target2[0].a.text
print(subque4)
```
<br/>

- Sample 14: 屬性子查詢
```
from urllib import request
from bs4 import BeautifulSoup
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

# find 已是單值物件，直接 .div 即可取出內層標籤
target1=soup.find("div", id="main-container")
# 以 ["屬性"] 取出 (注意：同層) 屬性
subque5=target1.div["id"]
print(subque5)

# findAll 為清單，需取出首項物件方可進取內層標籤
target2=soup.findAll("div", id="main-container")
# 以 ["屬性"] 取出 (注意：同層) 屬性
subque6=target2[0].a["class"]
print(subque6)
```
