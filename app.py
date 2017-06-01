import sys
import telegram
from flask import Flask, request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

API_TOKEN = '380967545:AAFeYaTwq8QhqdV0W69cjnICVJCq5PDmXrc'
WEBHOOK_URL = 'https://f96dc639.ngrok.io/hook'
PHANTOMJS_PATH = 'phantomjs-2.1.1-windows/bin/phantomjs'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
global state
state=0
global start
start=''
global end
end=''

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)

def message0(text,client_id):
    global state
    if text=='/start':
        bot.sendMessage(chat_id=client_id, text='Hello,歡迎使用SeoulPass\n請從【天氣】【匯率】【地鐵】三項中選擇一項輸入')
    elif text=='匯率':
        bot.sendMessage(chat_id=client_id, text="請輸入韓圜(KWR)金額")
        state=1
    elif text=='天氣':
        res=requests.get("http://www.accuweather.com/zh/kr/seoul/226081/daily-weather-forecast/226081?lang=zh-tw")
        soup=BeautifulSoup(res.text,"html.parser")
        weather=soup.select('.info-wrapper')
        weather1=soup.find_all('strong')
        TEXT=u'1.高溫:'+weather[0].select('.large-temp')[0].text[0:3]+u'C\n2.體感溫度:'+weather[0].select('.realfeel')[0].text[-3:]+u'C\n3.降雨機率:'+weather[0].select('.precip')[0].text[-3:]+u'\n4.紫外線指數:'+weather1[4].text+u'\n5.陣風:'+weather1[3].text+'\n'+weather[0].select('.cond')[0].text.replace(' ','').replace('\n','')
        TEXT1=u'1.高溫:'+weather[1].select('.large-temp')[0].text[0:3]+u'C\n2.體感溫度:'+weather[1].select('.realfeel')[0].text[-3:]+u'C\n3.降雨機率:'+weather[1].select('.precip')[0].text[-3:]+u'\n4.陣風:'+weather1[13].text+'\n'+weather[1].select('.cond')[0].text.replace(' ','').replace('\n','')
        bot.sendMessage(chat_id=client_id, text='【首爾天氣】白天\n'+TEXT.encode('utf-8'))
        bot.sendMessage(chat_id=client_id, text='【首爾天氣】夜晚\n'+TEXT1.encode('utf-8'))
        state=0
    elif text=='地鐵':
        bot.sendMessage(chat_id=client_id, text="請輸入起始站名稱")
        state=2
    else:
        bot.sendMessage(chat_id=client_id, text='請從【天氣】【匯率】【地鐵】三項中選擇一項輸入')


def message1(text,client_id):
    global state
    if text=='匯率':
        bot.sendMessage(chat_id=client_id, text="請輸入韓圜(KWR)金額")
        state=1
    elif int(text)>=0:
        res=requests.get("https://tw.money.yahoo.com/currency-converter")
        soup=BeautifulSoup(res.text,"html.parser")
        T=soup.find_all('td','end')
        twd=int(text)*float(T[21].text.encode('utf-8'))        
        bot.sendMessage(chat_id=client_id, text= str(twd)+'台幣(TWD)')
        state=0

def message2(text,client_id):
    global state    
    global start
    if text=='地鐵':
        bot.sendMessage(chat_id=client_id, text="請輸入起始站名稱")
        state=2
    if text.find('站')>0:
        file1 = open('station.txt','r')
        for line in file1:
            a=line.split(' ')
            if a[1].replace('\n', '')==text.replace('站', ''):
                start=a[0]
                bot.sendMessage(chat_id=client_id, text="請輸入終點站名稱")
                break
        state=3
    else:
        file1 = open('station.txt','r')
        for line in file1:
            a=line.split(' ')
            if a[1].replace('\n', '')==text:
                start=a[0]
                bot.sendMessage(chat_id=client_id, text="請輸入終點站名稱")
                break
        state=3

def message3(text,client_id):
    global state
    global start
    global end
    if text=='地鐵':
        bot.sendMessage(chat_id=client_id, text="請輸入起始站名稱")
        state=2
    if text.find('站')>0 :
        file1 = open('station.txt','r')
        for line in file1:
            a=line.split(' ')
            if a[1].replace('\n', '')==text.replace('站', ''):
                end=a[0]
                break
    else:
        file1 = open('station.txt','r')
        for line in file1:
            a=line.split(' ')
            if a[1].replace('\n', '')==text:
                end=a[0]
                break
    if start!="" and end!="":
        driver = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
        driver.get('http://www.smrt.co.kr/program/cyberStation/main2.jsp?lang=c1&stcd2='+start+'&stcd3='+end)
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "html.parser")
        start_st=soup.select('#startStationName')
        end_st=soup.select('#endStationName')
        time=soup.select('.point1')
        stop_st=soup.select('#stopStationLength')
        distance=soup.select('#distance')
        price=soup.select('#card_adu_fare')
        transfer=soup.select('em')
        if len(transfer)==9:
            t1=u"【起始站】"+start_st[0].text+u"\n【終點站】"+end_st[0].text+u"\n【兩站之間距離】"+distance[0].text+u"公里\n【所需時間】"+time[0].text.replace('about ', '')+u"\n【途中停靠車站數量】"+stop_st[0].text+u"站\n【價錢】"+price[0].text.replace('won', '')+u"韓圜(KWR)"
            bot.sendMessage(chat_id=client_id, text=t1)
        if len(transfer)==10:
            t2=u"【起始站】"+start_st[0].text+u"\n【轉車站】"+transfer[0].text+u"\n【終點站】"+end_st[0].text+u"\n【兩站之間距離】"+distance[0].text+u"公里\n【所需時間】"+time[0].text.replace('about ', '')+u"\n【途中停靠車站數量】"+stop_st[0].text+u"站\n【價錢】"+price[0].text.replace('won', '')+u"韓圜(KWR)"
            bot.sendMessage(chat_id=client_id, text=t2)
        if len(transfer)==11:
            t3=u"【起始站】"+start_st[0].text+u"\n【轉車站】"+transfer[0].text+u"、"+transfer[1].text+u"\n【終點站】"+end_st[0].text+u"\n【兩站之間距離】"+distance[0].text+u"公里\n【所需時間】"+time[0].text.replace('about ', '')+u"\n【途中停靠車站數量】"+stop_st[0].text+u"站\n【價錢】"+price[0].text.replace('won', '')+u"韓圜(KWR)"
            bot.sendMessage(chat_id=client_id, text=t3)
        state=0
    else:
        bot.sendMessage(chat_id=client_id, text="站名輸入錯誤無法計算，請再從【天氣】【匯率】【地鐵】三項中選擇一項輸入")
        state=0

@app.route('/hook', methods=['POST'])
def webhook_handler():
    global state
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')
        if text=="Reset":
            state=0
            bot.sendMessage(chat_id=chat_id , text="狀態已重新設置，請從【天氣】【匯率】【地鐵】三項中選擇一項輸入")
        else:
            if text!="" and state==0:
                message0(text,chat_id)
            elif text!="" and state==1:
                message1(text,chat_id)
            elif text!="" and state==2:
                message2(text,chat_id)        
            elif text!="" and state==3:
                message3(text,chat_id)

    return 'ok'


if __name__ == "__main__":
    _set_webhook()
    app.run()
