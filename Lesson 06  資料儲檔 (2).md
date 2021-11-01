<h2 align="center">Lesson 06: 資料儲檔 (2)</h2>

- Sample 24: Pandas
```python
from urllib import request
from bs4 import BeautifulSoup

import pandas
# 宣告 DataFrame，並定義資料欄位
data=pandas.DataFrame(columns=["文章標題", "文章網址"])
# loc=index，以迴圈逐筆寫入資料
loc=0
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 輸出所有文章標題及網址
target=soup.findAll("div", {"class":"title"})
for item in target:
    title=item.a.text
    url="https://www.ptt.cc"+item.a["href"]

    # 列表逐項寫入，迴圈初始須清空
    datarow=[]
    datarow.append(title)
    datarow.append(url)
    data.loc[loc]=datarow
    loc+=1
print(data)
```
<br/>

- Sample 25: Pandas+csv 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import pandas
import os
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)

# 宣告 DataFrame，並定義資料欄位
data=pandas.DataFrame(columns=["文章標題", "文章網址"])
# loc=index，以迴圈逐筆寫入資料
loc=0
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 輸出所有文章標題及網址
target=soup.findAll("div", {"class":"title"})
for item in target:
    title=item.a.text
    url="https://www.ptt.cc"+item.a["href"]

    # 列表逐項寫入，迴圈初始須清空
    datarow=[]
    datarow.append(title)
    datarow.append(url)
    data.loc[loc]=datarow
    loc+=1
data.to_csv("%s/CSV.csv"%(dir), encoding="utf-8")
```
<br/>

- Sample 26: Pandas+xls 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import pandas
import os
import xlwt
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)

# 宣告 DataFrame，並定義資料欄位
data=pandas.DataFrame(columns=["文章標題", "文章網址"])
# loc=index，以迴圈逐筆寫入資料
loc=0
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 輸出所有文章標題及網址
target=soup.findAll("div", {"class":"title"})
for item in target:
    title=item.a.text
    url="https://www.ptt.cc"+item.a["href"]

    # 列表逐項寫入，迴圈初始須清空
    datarow=[]
    datarow.append(title)
    datarow.append(url)
    data.loc[loc]=datarow
    loc+=1
data.to_csv("%s/XLS.xls"%(dir), encoding="utf-8")
```
<br/>

- Sample 27: Pandas+xlsx 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import pandas
import os
import openpyxl
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)

# 宣告 DataFrame，並定義資料欄位
data=pandas.DataFrame(columns=["文章標題", "文章網址"])
# loc=index，以迴圈逐筆寫入資料
loc=0
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 輸出所有文章標題及網址
target=soup.findAll("div", {"class":"title"})
for item in target:
    title=item.a.text
    url="https://www.ptt.cc"+item.a["href"]

    # 列表逐項寫入，迴圈初始須清空
    datarow=[]
    datarow.append(title)
    datarow.append(url)
    data.loc[loc]=datarow
    loc+=1
data.to_csv("%s/XLSX.xlsx"%(dir), encoding="utf-8")
```
