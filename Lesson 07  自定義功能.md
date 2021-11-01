<h2 align="center">Lesson 07: 自定義功能</h2>

- Sample 28
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

file=open("%s/%s.txt"%(dir, filename)), "w", encoding="utf-8")
file.write(str(soup))
file.close()
```
<br/>

- Sample 29: Try/except
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

target=soup.findAll("div", {"class":"title"})
for item in target:
    try:
        title=item.a.text
        # 內迴圈開檔，附加 (a-mode) 續寫
        file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
        file.write(title+"\n")
        file.close()    
    # 當 title=none (如文章被刪除) 則 raise AttributeError
    except AttributeError:
        file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
        file.write("此文已被刪除"+"\n")
        file.close()
```
<br/>

- Sample 30
```python
from urllib import request
from bs4 import BeautifulSoup

import os
# 使用者自訂檔案存放路徑
dir=input("輸入檔案路徑：")
filename=input("輸入檔名：")
# 檢查：若無則創建、有則存入
if not os.path.exists(dir):
    os.mkdir(dir)
headers={"User-Agent":"***"}
url="https://www.ptt.cc/bbs/joke/index.html"

req=request.Request(url=url, headers=headers)
res=request.urlopen(req)
soup=BeautifulSoup(res, "html.parser")

error=0
target=soup.findAll("div", {"class":"title"})
for item in target:
    try:
        title=item.a.text
        # 內迴圈開檔，附加 (a-mode) 續寫
        file=open("%s/%s.csv"%(dir, filename), "a", encoding="utf-8")
        file.write(title+"\n")
        file.close()   
    # 當 title=none (如文章被刪除) 則 raise AttributeError
    except AttributeError:
        error+=1

print("爬蟲結束，有 %d 篇文章已被刪除"%(error))
```
