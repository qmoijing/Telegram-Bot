# Telegram-Bot
Bot Name:SeoulPass<br />
Bot Username:SeoulPass_Bot<br />
由於暑假時要和朋友去首爾自助旅行，因此藉由這次的Project去實作一個包含首爾天氣、地鐵資訊、匯率換算這三個功能的聊天機器人

## Setup

### Prerequisite
* Python 2.7
#### Install Dependency
* python-telegram-bot
* pygraphviz
* Flask
```sh
pip install virtualenv
pip install Flask 
```
* beautifulsoup4
```sh
pip install beautifulsoup4
```
* selenium 和 PhantomJS
  1.  先安裝 python selenium 套件
  ```sh
  pip install selenium
  ```
  2.  下載並解壓縮 PhantomJS 軟體，檔案路徑在python程式碼中會用上<br />
  下載位置：http://phantomjs.org/download.html
  
### Secret Data
app.py中【API_TOKEN】【WEBHOOK_URL】【PhantomJS 檔案路徑】 需要設置成適當的值

### How to Run


### Hou to Use
#### 首爾天氣
輸入"天氣" -> Bot回傳**當天首爾天氣資訊**<br />
![weather](./img/weather.jpg)
#### 匯率換算
輸入"匯率" -> Bot回傳"請輸入韓圜金額" -> 輸入**數字** -> Bot回傳**所對應的台幣金額**
#### 地鐵資訊
輸入"地鐵" -> Bot回傳"請輸入起始站" -> 輸入**起始站** -> Bot回傳"請輸入終點站" -> 輸入**終點站** ->  Bot回傳**地鐵資訊**
