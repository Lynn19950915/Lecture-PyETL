<h2 align="center">Lesson 01: 爬網初覽</h2>

- Sample 01
```python
# 引入 request (不可只寫 import urllib)
from urllib import request

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)

# 會顯示 b'\n... (代表 bytes，為非制式之原始碼標籤字串)
print(res.read())
```
<br/>

- Sample 02: decode("utf-8")
```python
# 引入 request (不可只寫 import urllib)
from urllib import request

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)

# 以 utf-8 將所獲訊息 (res) 進行解碼
print(res.read().decode("utf-8"))
```
<br/>

- Sample 03: BeautifulSoup("html.parser")
```python
# 引入 request (不可只寫 import urllib)
from urllib import request
# 引入 BeautifulSoup (不可只寫 import bs4)
from bs4 import BeautifulSoup

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)

# 以 BeautifulSoup 將所獲訊息 (res) 進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")
print(soup)
```
