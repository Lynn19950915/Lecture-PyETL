<h2 align="center">Lesson 05: 資料儲檔 (1)</h2>

- Sample 19: txt 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

# 開檔寫入 (w-mode)
file=open("%s/TXT.txt"%(dir)), "w", encoding="utf-8")
# 以字串型態寫入檔案
file.write(str(soup))
file.close()
```
<br/>

- Sample 20: csv 檔：內迴圈
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
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

    # 內迴圈開檔，附加 (a-mode) 續寫
    file=open("%s/CSV.csv"%(dir), "a", encoding="utf-8")
    file.write(title+url+"\n")
file.close()
```
<br/>

- Sample 21: csv 檔：雙迴圈
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

datarow=[]
loc=0
# 輸出所有文章標題及網址
target=soup.findAll("div", {"class":"title"})
for item in target:
    title=item.a.text
    url="https://www.ptt.cc"+item.a["href"]

　　# 逐圈增寫一筆 (巢狀) 列表
    datarow.append([])
    datarow[loc].append(title)
    datarow[loc].append(url)
    loc+=1

file=open("%s/CSV.csv"%(dir), "w", encoding="utf-8")
for rows in datarow:
    # 外迴圈 writelines：逐項列表輸出
    file.writelines(rows)
    file.write("\n")
file.close()
```
<br/>

- Sample 22: xls 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import os
import xlwt
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
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

    file=open("%s/XLS.xls"%(dir), "a", encoding="utf-8")
    file.write(title+url+"\n")
file.close()
```
<br/>

- Sample 23: xlsx 檔
```python
from urllib import request
from bs4 import BeautifulSoup

import os
import openpyxl
# 新增一資料夾存放檔案
dir="C:/PyETL"
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
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

    file=open("%s/XLSX.xlsx"%(dir), "a", encoding="utf-8")
    file.write(title+url+"\n")
file.close()
```
