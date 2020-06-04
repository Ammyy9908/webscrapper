from bs4 import BeautifulSoup
import requests

url = 'https://stackoverflow.com/questions/59949835/access-element-of-list-as-dict'

response = requests.get(url)
#print(response)
soup = BeautifulSoup(response.text,'html.parser')
answers = soup.findAll('div',{'class':'answer'})
for answer in answers:
      vote = answer.find('div',{'class':'js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center'})
      solution = answer.find('div',{'class':'post-text'})
      vote_count = str(vote.text)
      vote_count = int(vote_count)
      if vote_count > 10:
             print(vote.text)
             print(solution.code.text)

     