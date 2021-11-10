from bs4 import BeautifulSoup
import requests

# Initialization for http request
athens = 'https://weather.com/el-GR/weather/today/l/dd331ef7b39406c08b339ad503f0d9475cb742124d8753ae20750e72051e91c1'
thess = 'https://weather.com/el-GR/weather/today/l/4f7940e96197643c80e3c64a7d0ccb4fb6eff7bced4158152da995da08f40053'
patra = 'https://weather.com/el-GR/weather/today/l/a8c1d5fa8f854f3e5c626109483f1542b6eb8f29924330ccc44ffc07e3050bd7'
gianena = 'https://weather.com/el-GR/weather/today/l/7a5351e10b7d52f667e9f0a0b71140bd176ef6cd09edf748f7e28a607baeb3e8'
hrakleio = 'https://weather.com/el-GR/weather/today/l/4f3800462bc69d7213931d2a3ed41b2ea6f1e8ce1925bfdce551292d2d6fdb44'

high_temp = -99
temperatures = []
i =0
high_temp_printed = False
cities = [athens, thess, patra, gianena, hrakleio]

for city in cities:
    # Do http requests
    source = requests.get(city).text
    # Parsing the site with lxml Parser
    soup = BeautifulSoup(source, 'lxml')

    # Scraping
    city = soup.find('h1', class_= 'CurrentConditions--location--kyTeL').text
    temperature = soup.find('span', class_='CurrentConditions--tempValue--3a50n').text
    rain = soup.find('div', class_='CurrentConditions--precipValue--3nxCj').text

    temp_int = int(temperature[0:2])

    # Find the city with highest temperature 
    if temp_int > high_temp:
        high_temp = temp_int
        city_high_temp = soup.find('h1', class_='CurrentConditions--location--kyTeL').text
        j=i
        i+=1
        high_temp_printed = False

    print(city)
    print(temperature)
    print(rain+"\n")

if high_temp_printed == False:
    print("Η πόλη με την μέγιστη θερμοκρασία")
    print(city_high_temp)
    print(temperature)
    high_temp_printed=True


