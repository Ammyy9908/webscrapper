from bs4 import BeautifulSoup
import requests
import pyttsx3



def get_info(country='india'):
      url = 'https://www.worldometers.info/coronavirus/country/{}/'.format(country)
      try:
            response = requests.get(url)
            #print(response)
            soup = BeautifulSoup(response.text,'html.parser')
            data = soup.findAll('div',{'class':'maincounter-number'})
            print("Current Covid-19 India Report")
            new_data = []
            for tc in range(0,len(data)):
                  new_data.append(data[tc].text)
           
            
            
            print(f"Total Cases: {new_data[0]}".rstrip())
            print(f"Total Deaths: {new_data[1]}".rstrip())
            print(f"Total Recovered: {new_data[2]}".rstrip())
            engine = pyttsx3.init()
            engine.setProperty('rate',200)
            engine.say(f'Total Cases in {country} is {new_data[0]} and Total Deaths are {new_data[1]}')
            engine.say(f'Total Recovered Cases are {new_data[2]}')
            engine.runAndWait()
      except :
            print("No Internet Connection")


while(1):
      print("1.Get Covid-19 Report\n2.Exit")
      ch = input("Choose Your Choice:")
      if ch == "1":
            country = input('Enter the Country!')
            get_info(country)
      elif ch == "2":
            exit()
      else:
            print("Invalid Choice")
      



            
