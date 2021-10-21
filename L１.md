Lesson 01　爬網初覽

<p>1.1</p>
<pre>
# 引入request(不可只寫import urllib)
from urllib import request

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)

print(res.read())
* 顯示:b'\n...(代表bytes，非制式之原始碼標籤字串)
</pre>


<p>1.2　decode("utf-8")</p>
<pre>
# 引入request(不可只寫import urllib)
from urllib import request

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)

#以utf-8將所獲訊息(res)進行解碼
print(res.read().decode("utf-8"))
</pre>


<p>1.3　BeautifulSoup("html.parser")</p>
<pre>
#引入request(不可只寫import urllib)
from urllib import request
#引入BeautifulSoup(不可只寫import bs4)
from bs4 import BeautifulSoup

url="https://www.businessweekly.com.tw/channel/englishlearning/0000000335"
res=request.urlopen(url)
#以BeautifulSoup將所獲訊息(res)進行解碼，且可被定位
soup=BeautifulSoup(res, "html.parser")

print(soup)
</pre>
