import requests
url = "https://food.trueid.net/detail/531N4RM0qy8x"
data = requests.get(url)
data.encoding ='utf-8'
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all("a") 
print(x)