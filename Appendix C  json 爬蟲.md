<h2 align="center">Appendix C: json 爬蟲</h2>

- Sample C1
```python
from urllib import request
from bs4 import BeautifulSoup
import json
headers={"User-Agent":"***"}
url="https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232618563"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)

soup=BeautifulSoup(res, "html.parser")
# loads 可將字串轉為 json 物件，故 soup 需先轉換
jslist=json.loads(str(soup))
for item in jslist:
    #一篇文就是一本字典
    print(item)
```
<br/>

- Sample C2: #Dcard 攝影版
```python
from urllib import request
from bs4 import BeautifulSoup
import json

# pandas 框架搭配 xls 檔案輸出
import pandas
import xlwt
article=pandas.DataFrame(columns=["網址", "標題", "時間", "文章內容", "讚數", "留言數"])
loc=0
headers={"User-Agent":"***"}
url="https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232618563"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

jslist=json.loads(str(soup))
for item in jslist:
    content=[]
    # 網址由固定結構 +id 組成，連接需轉為字串
    content.append("https://www.dcard.tw/f/photography/p/"+str(item["id"]))
    content.append(item["title"])
    content.append(item["createdAt"])
    content.append(item["excerpt"])
    content.append(item["likeCount"])
    content.append(item["commentCount"])
    # 逐筆 row-index 寫入列表中 
    article.loc[loc]=content
    loc+=1

print("爬蟲結束，共計 %d 篇文章"%(loc))
article.to_excel("C:/PyETL/Dcard攝影版.xls", encoding="utf-8")
```
<br/>

- Sample C3: #Weather API
```python
from urllib import request
from bs4 import BeautifulSoup
import json

# pandas 框架搭配 xls 檔案輸出
import pandas
import xlwt
article=pandas.DataFrame(columns=["鄉鎮代碼", "概況", "溫度", "體感溫度", "濕度", "雨量"])
headers={"User-Agent":"***"}

countyId=1
while countyId <=368:
    url="https://works.ioa.tw/weather/api/weathers/%d.json"%(countyId)
    req=request.Request(url=url, headers=headers)
    res=request.urlopen(req)
    soup=BeautifulSoup(res, "html.parser")

    jslist=json.loads(str(soup))
    content=[]
    content.append(countyId)
    content.append(jslist["desc"])
    content.append(jslist["temperature"])
    content.append(jslist["felt_air_temp"])
    content.append(jslist["humidity"])
    content.append(jslist["rainfall"])
    # 逐筆 row-index 寫入列表中 
    article.loc[countyId-1]=content
    countyId+=1

article.to_excel("C:/PyETL/Weather_API.xls", encoding="utf-8")
```
