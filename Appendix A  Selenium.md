<h2 align="center">Appendix A: Selenium</h2>

- Sample A1: get
```
# 需先安裝 selenium 及下載 Chrome driver
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver")
url="https://www.ptt.cc/bbs/index.html"

# 提出請求，執行後將自動開啟一瀏覽分頁
driver.get(url)
```
<br/>

- Sample A2: find, click
```
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver")
url="https://www.ptt.cc/bbs/index.html"

driver.get(url)
# 以 class name 尋找標籤，並自動點擊
driver.find_element_by_class_name("board-name").click()
# 同理，亦以此點擊年齡分級管理頁面
driver.find_element_by_class_name("btn-big").click()
```
<br/>

- Sample A3: cookies
```
from selenium.webdriver import Chrome
driver=Chrome("./chromedriver")
url="https://www.ptt.cc/bbs/index.html"

driver.get(url)
driver.find_element_by_class_name("board-name").click()
driver.find_element_by_class_name("btn-big").click()

# 取得 cookies 資訊並印出
cookies=driver.get_cookies()
for item in cookies:
    print(item)
```
<br/>

- Sample A4
```
from selenium.webdriver import Chrome
import requests
from bs4 import BeautifulSoup
driver=Chrome("./chromedriver")
url="https://www.ptt.cc/bbs/index.html"

driver.get(url)
driver.find_element_by_class_name("board-name").click()
driver.find_element_by_class_name("btn-big").click()

cookies=driver.get_cookies()
driver.close()
# 以 session 搭配 requests.get(url, cookies) 發送請求
ss=requests.session()
for item in cookies:
    ss.cookies.set(item["name"], item["value"])

res=ss.get("https://www.ptt.cc/bbs/Gossiping/index.html")
# requests 需加註 .text，使用 prettify 輸出結構
soup=BeautifulSoup(res.text, "html.parser")
print(soup.prettify())
```
