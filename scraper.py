import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.weather2day.co.il/tel-aviv")
soup = BeautifulSoup(page.content, 'html.parser')
weather = soup.find(id='ecmwf')
what = weather.find_all('time')
what2 = weather.find_all('span')
j=0
for i in range(10):
    print(what[i].get_text())
    print(what2[j].get_text() + " - " + what2[j+1].get_text())
    j+2
