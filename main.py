import requests
from bs4 import BeautifulSoup
from Indicator import Indicator

url = 'https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'lxml')

indicators = soup.findAll('dl', 'class')
lista = list()
for indicator in indicators:
    title = indicator.find('code', 'sig-name descname').text
    params = indicator.findAll('em', 'sig-param')
    indicatorObject = Indicator(title)
    indicatorObject.setParams(params)
    print(indicatorObject)

