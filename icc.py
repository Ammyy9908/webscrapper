from bs4 import BeautifulSoup
import requests

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/test'

response = requests.get(url)
print(response)

# parsing

soup = BeautifulSoup(response.text,'html.parser')

table = soup.find('div',{'class':'rankings-block__container full rankings-table'})
for team in table.find_all('td',{'class':'table-body__cell rankings-table__team'}):
      for teamname in team.find_all('span',{'class':'u-hide-phablet'}):
            print(teamname.text)