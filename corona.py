from bs4 import BeautifulSoup
import requests

url = 'https://www.mygov.in/covid-19'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

active = soup.find('div',{'class':'iblock active-case'}).find('div',{'class':'iblock_text'}).find('span',{'class':'icount'}).text
discharge = soup.find('div',{'class':'iblock discharge'}).find('span',{'class':'icount'}).text
confirmed = int(str(active))+int(str(discharge))
deaths = soup.find('div',{'class':'iblock death_case'}).find('span',{'class':'icount'}).text
migrated = soup.find('div',{'class':'iblock migared_case'}).find('span',{'class':'icount'}).text
print("Latest Covid-19 India Report")
print("Total Confirmed: {}".format(confirmed))
print("Active Case : {}".format(active))
print("Total Discharged: {}".format(discharge))
print("Total Deaths: {}".format(deaths))
print("Migrated : {}".format(migrated))
states_name = soup.find('div',{'id':'stateCount'}).findAll('span',{'class':'st_name'})
states_count = soup.find('div',{'id':'stateCount'}).findAll('span',{'class':'st_number'})
print("\nState Wise Report:")
print()
print("State || Count")
for i in range(0, len(states_count)):
      print("{}||{}".format(states_name[i].text,states_count[i].text))
