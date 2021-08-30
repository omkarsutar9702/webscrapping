import requests
from bs4 import BeautifulSoup
import time
import csv
import mail
from datetime import date

urls = ['https://finance.yahoo.com/quote/TSLA/',"https://finance.yahoo.com/quote/ASHOKLEY.NS?p=ASHOKLEY.NS&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMZN?p=AMZN","https://finance.yahoo.com/quote/CL?p=CL&.tsrc=fin-srch"]

today = str(date.today())+".csv"

csv_file=open(today,"w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['stockname','current_price','previous_close','open','bid','ask','days range','52 week range','volume','avg.volmue'])

for url in urls:
    stock =[]
    headers= {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    html_page = requests.get(url ,headers=headers)
    soup = BeautifulSoup(html_page.content,'lxml')

    title = soup.find_all("div",class_="D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)")[0].find("h1").get_text()
    current_price = soup.find_all("div",class_="My(6px) Pos(r) smartphone_Mt(6px)")[0].find("span").get_text()
    
    stock.append(title)
    stock.append(current_price)
    table_info= soup.find_all("div",class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')[0].find_all("tr")

    for i in range(0,8):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)
    
    csv_writer.writerow(stock)
    time.sleep(5)    
csv_file.close()
mail.send_mail(filename=today)