import requests
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import time


def send_to_email(news):
      from_address = '1mv19is404@sirmvit.edu'
      # list of users
      recpient_list = ['sb78639@gmail.com','1mv19is403@sirmvit.edu','tabhishek2007@gmail.com']
      msg = MIMEMultipart()
      msg['From']=formataddr((str(Header('PythoNews', 'utf-8')), '1mv19is404@sirmvit.edu'))
      
      msg['Subject']='Your Daily News'
      news_data = news
      html ='''<html>
      <head>
      <title>PythoNews -Your Daily News</title>
      <style>
      .title
      {
            
            color:red;
            font-size:2rem;
      }
      .subtitle
      {
            color:#000;
            font-size:18px;
      }
      a
      {
            text-decoration:none;
      }

      
      </style>
      </head>
      <body bgcolor="red">
      '''
      for i in range(0, len(news_data)):
            html+=f'<div class="box"><h1 class="title">{news_data[i][0]}</h1>\n<p class="subtitle">{news_data[i][1]}</p></div>\n<a href="{news_data[i][2]}">Read Full Post</a>'
      html +='</body></html>'
      msg.attach(MIMEText(html,'html'))
      # creates SMTP session 
      s = smtplib.SMTP('smtp.gmail.com', 587) 
      s.ehlo()
      s.starttls()
      s.ehlo()
      s.login(from_address,'sirmvit123')
      text = msg.as_string()
      for i in recpient_list:
            msg['To']=i
            s.sendmail(from_address,i,text)
      s.quit()
      print("Your Daily News Sented")
      

      
      


url = 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=77fcc3b8e0e44caa9df1f04080fb1fdf'

response = requests.get(url)
data = response.json()
data=data['articles']

titles = list()
description = list()
urls = list()

for i in range(0,len(data)):
      titles.append(data[i]['title'])
      description.append(data[i]['description'])
      urls.append(data[i]['url'])



parsedData = tuple(zip(titles,description,urls))

while True:
      send_to_email(parsedData)
      time.sleep(3600) # 1hour = 3600 seconds
      # calling the same function after 1 hour










