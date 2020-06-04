from bs4 import BeautifulSoup
import requests
import webbrowser
import os


keyword = input('Enter the topic!\n')
url = 'https://www.brainyquote.com/topics/{}'.format(keyword)
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
quote = soup.find('div',{'id':'quotesList'}).find_all('div',{'class':'clearfix'})
new_list = list()
author_list = list()
for i in quote:
      for j in i.findAll('a',{'class':'b-qt'}):
            new_list.append(j.text.strip())
for j in quote:
      for k in j.findAll('a',{'class':'bq-aut'}):
            author_list.append(k.text.strip())

count = 1
data = ''''''
for index in range(0,len(new_list)):
      
      data+=f'''<div class="columns">
      <div class="column">
      <div class="content is-medium">
      <h5 class="subtitle is-size-5">"{new_list[index]}"</h5>
                <p class="subtitle has-text-link">by {author_list[index]}</p>
              </div>
            </div></div>'''
      count += 1






template = f'''
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>{keyword} Quotes </title>
  <link rel="stylesheet" href="https://unpkg.com/bulma@0.8.2/css/bulma.min.css" />
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"
    integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <link rel="stylesheet" href="../css/bulma-divider.min.css">

</head>

<body>
  <!-- START NAV -->
  <nav class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item" href="../">
          <strong>{keyword} Quotes</strong>
        </a>
        <span class="navbar-burger burger" data-target="navbarMenu">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
      
    </div>
  </nav>
  <!-- END NAV -->

  <!-- Image -->
  <section class="hero ">
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column is-8 is-offset-2">
            <figure class="image is-16by9">
              <img src="https://source.unsplash.com/1600x900/?{keyword}" alt="">
            </figure>
          </div>
        </div>

        <section class="section">
          

          {data}
            
        
        </section>



      </div>
    </div>
  </section>

  
</body>

</html>
'''

with open(f'quotes/{keyword}.html','w') as file:
      file.write(template)
      print("Quotes Saved")
      

cwd = os.getcwd()
url = f'file:///{cwd}/quotes/{keyword}.html'
webbrowser.open(url, new=2)
      

      


      

