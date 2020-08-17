import requests
import json


products_raw = requests.get('https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/products.json').text
products = json.loads(products_raw)

ingredients_raw = requests.get('https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json').text

ingredients = json.loads(ingredients_raw)
