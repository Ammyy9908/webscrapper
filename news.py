from bs4 import BeautifulSoup
import requests

city = input('Enter the Keyword to search\n')
url = 'https://economictimes.indiatimes.com/topic/{}/news'.format(city)

response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text,'html.parser')

soup = soup.find_all('li',{'id':'news'})
#print(soup)

for data in soup:
      for headings in data.findAll('h3'):
            for desc in data.findAll('p'):
                  for links in data.findAll('a'):
                        for i in range(0,10):
                              print('Heading-> '+str(headings.text)+'\n\n Description-> '+str(desc.text)+' \n\nPost URL-->https://economictimes.indiatimes.com/'+links['href'])
                              print()
                  
      