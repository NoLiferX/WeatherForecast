from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier as tn

# Initialization for http request
tokyo = 'https://weather.com/en-GB/weather/today/l/4ba28384e2da53b2861f5b5c70b7332e4ba1dc83e75b948e6fbd2aaceeeceae3'
osaka = 'https://weather.com/en-GB/weather/today/l/49fbadf46d6a950673c54e4427ce9371b45e617247efda03fed276143dfc65ba'
kyoto = 'https://weather.com/en-GB/weather/today/l/db404793036d55e5d1404643882f997027bf2093c64b4127ad7a969054ed393c'
nagoya = 'https://weather.com/en-GB/weather/today/l/096fc9d3995db272f638412ce2bc0de4104bffbf25224e20178a67973dd35845'
kobe = 'https://weather.com/en-GB/weather/today/l/b805f3d0d33367259525091ec49cc64f614f4c88b10af0c29abf0927e872ab66'

# Initialization others variables
high_temp = -99
temperatures = []
i =0
high_temp_printed = False
cities = [tokyo, osaka, kyoto, nagoya, kobe]

for city in cities:
    # Do http requests
    source = requests.get(city).text
    # Parsing the site with lxml Parser
    soup = BeautifulSoup(source, 'lxml')

    # Scraping
    city = soup.find('h1', class_= 'CurrentConditions--location--kyTeL').text
    index = city.find(",")
    city = city[:index]
    temperature = soup.find('span', class_='CurrentConditions--tempValue--3a50n').text
    temp_int = int(temperature[0:2])
    rain = soup.find('div', class_='CurrentConditions--precipValue--3nxCj').text

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


