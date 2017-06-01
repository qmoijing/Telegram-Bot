# Telegram-Bot
Bot Name:SeoulPass<br />
Bot Username:SeoulPass_Bot<br />
藉由這次的Project去實作一個包含首爾天氣、地鐵資訊、匯率換算這三個功能的聊天機器人

## Setup
### 操作環境
* Windows 8<br />
* 虛擬機：Oracle VM VirtualBox<br />
  * Ubuntu Linux 32位元(執行draw_fsm.py)
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

## How to Run
### Run ngrok
1.先申請帳號，並下載ngrok<br />
2.開啟ngrok
```sh
ngrok authtoken token
```
```sh
ngrok http localhost:5000
```
ngrok會產生https URL<br />
在app.py中的WEBHOOK_URL設置成ngrok產生的https URL
### Run the sever
開啟CMD進入專案的資料夾
```sh
python app.py
```
### Run telegram
使用telegram Desktop，並與Bot開始對話

## Hou to Use
### 首爾天氣
輸入"天氣" -> Bot回傳**當天首爾天氣資訊**<br />
![weather](/img/weather.JPG)

### 匯率換算
輸入"匯率" -> Bot回傳"請輸入韓圜金額" -> 輸入**數字** -> Bot回傳**所對應的台幣金額**<br />
![money](/img/money.JPG)

### 地鐵資訊
輸入"地鐵" -> Bot回傳"請輸入起始站" -> 輸入**起始站** -> Bot回傳"請輸入終點站" -> 輸入**終點站** ->  Bot回傳**地鐵資訊**<br />
> * 因為地鐵站尚未整理完，因此請先輸入station.txt中有的地鐵站名
> * Bot回傳地鐵資訊需要等待大約1分鐘的時間，因為selenium要執行網站中javascript的部分

![MRT](/img/MRT.JPG)

## Finite State Machine
![fsm](/img/fsm.png)
