import requests
from bs4 import BeautifulSoup

url = 'https://www.webscraper.io/test-sites/e-commerce/ajax'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', {'class': 'thumbnail'})

for product in products:
    name = product.find('a', {'class': 'title'}).text.strip()
    description = product.find('p', {'class': 'description'}).text.strip()
    price = product.find('h4', {'class': 'price'}).text.strip()

    print(f'Name: {name}')
    print(f'Description: {description}')
    print(f'Price: {price}')
    print('-----------------------')