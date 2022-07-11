import requests
from bs4 import BeautifulSoup

'''headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
url = "https://www.transfermarkt.com/"
r = requests.get(url, headers=headers)
print(r.status_code)
'''
html_doc ="""<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.p)
print(soup.find('p'),'\n')

print(soup.find('a')['href'])
print(soup.a['href'],'\n')

print(soup.find('a').text)
print(soup.find('a').get_text(),'\n')

print(soup.find_all('a'))

print(soup.find_all('a')[1])

a_list = soup.find_all('a')
for i in a_list:
    print(i['href'])
    print(i. text,)
print('\n')

print(soup.find_all('a', class_='sister'))
print(soup.find_all('a', {'class':'sister'}),'\n')

print(soup.find_all('a', id='link3'))
print(soup.find_all('a', {'id':'link3'}),'\n')