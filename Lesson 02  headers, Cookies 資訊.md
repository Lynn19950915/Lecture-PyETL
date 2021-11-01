<h2 align="center">Lesson 02: headers, Cookies 資訊</h2>

- Sample 04: headers (字典)
```python
from urllib import request
# headers 為字典格式
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)

print(res.read().decode("utf-8"))
```
<br/>

- Sample 05
```python
from urllib import request
from bs4 import BeautifulSoup
# headers 為字典格式
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)

soup=BeautifulSoup(res, "html.parser")
print(soup)
```
<br/>

- Sample 06: header requests
```python
import requests
from bs4 import BeautifulSoup
# headers 為字典格式
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

# requests 無 urlopen 方法 (故 req, res 步驟合併)
res=requests.get(url=url, headers=headers)

# requests 無 read 方法，需藉 BeautifulSoup 解碼
soup=BeautifulSoup(res.text, "html.parser")
print(soup)
```
<br/>

- Sample 07: Cookies
```python
from urllib import request
from bs4 import BeautifulSoup
# headers, Cookies 為字典格式，寫在同一本
headers={"Cookie":"***", "User-Agent":"***"}
url="https://www.ptt.cc/bbs/Gossiping/index.html"

# 發送 request 時加上 headers 資訊
req=request.Request(url=url, headers=headers)
res=request.urlopen(req)

soup=BeautifulSoup(res, "html.parser")
print(soup)
```
<br/>

- Sample 08: Cookies requests
```python
import requests
from bs4 import BeautifulSoup
# headers, Cookies 為字典格式，分開寫兩本
headers={"User-Agent":"***"}
Cookies={"over18":"***"}
url="https://www.ptt.cc/Gossiping/joke/index.html"

# requests 無 urlopen 方法 (故 req, res 步驟合併)
res=requests.get(url=url, headers=headers, cookies=Cookies)

# requests 無 read 方法，需藉 BeautifulSoup 解碼
soup=BeautifulSoup(res.text, "html.parser")
print(soup)
```
