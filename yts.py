from bs4 import BeautifulSoup
import requests
import urllib.request

# request
url ='https://yts.mx/browse-movies/Horror/all/all/0/latest/0/all'

response = requests.get(url)

# use this response

soup = BeautifulSoup(response.text,'html.parser')

frames = soup.find_all('div',{'class':'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})

for i in frames:
      figure = i.find('figure')
      photo_url=figure.img['src']
      name = photo_url.split('/')
      name = name[-2]+name[-1]
      print('Downloading....{}'.format(name))
      urllib.request.urlretrieve(photo_url,'imgs/'+name)
