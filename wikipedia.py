from bs4 import BeautifulSoup
import requests
import os
print("Enter the Keyword to search on Wikipedia\n")
keyword = input()

url ='https://en.wikipedia.org/wiki/'+keyword

response = requests.get(url)
#print(response)
soup = BeautifulSoup(response.text,'html.parser')
soup = soup.find_all('p')
data = ""
for parsedData in soup:
      data +=str(parsedData.text)
os.mkdir('downloads/{}'.format(keyword))

with open('downloads/{}/{}.txt'.format(keyword,keyword),'w') as file:
      file.write(data)
      print("Your Data File is Ready!")