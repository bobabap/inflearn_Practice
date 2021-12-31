import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '5059341570:AAEn-QOaziFknTFVqoSB9qioUJ6RCt5bmlI')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0059&date=20220104'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    forDX = soup.select_one('span.forDX')
    if(forDX):
        forDX = forDX.find_parent('div', class_='col-times')
        title = forDX.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id= 5050970008, text=title + ' 4DX 예매가 열렸습니다.')
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()