import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.weather2day.co.il/tel-aviv")
soup = BeautifulSoup(page.content, 'html.parser')
weather = soup.find(id='ecmwf')
dates = weather.find_all('time')
temps = weather.find_all('span')
j=0
for i in range(10):
    print(dates[i].get_text())
    print(temps[j].get_text() + " - " + temps[j+1].get_text())
    j+2
