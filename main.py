import requests
from bs4 import BeautifulSoup

url = 'https://rozetka.com.ua/3d_glasses/c131143/'
response = requests.get(url)
page_content = response.text

soup = BeautifulSoup(page_content, 'html.parser')

discounted_products = []
items = soup.find_all('div', class_='goods-tile__inner')
for item in items:
    name = item.find('span', class_='goods-tile__title').text.strip()
    price = item.find('span', class_='goods-tile__price-value').text.strip()
    discount_tag = item.find('span', class_='goods-tile__discount-label')
    if discount_tag:
        discounted_products.append((name, price))

with open('discounted_products.txt', 'w', encoding='utf-8') as file:
    for product in discounted_products:
        file.write(f'{product[0]}: {product[1]}\n')