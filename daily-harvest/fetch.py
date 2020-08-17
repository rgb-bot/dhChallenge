import requests
import json

products_response = requests.get('https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/products.json')
products_raw = products_response.text
products = json.loads(products_raw)

ingredients_response = requests.get('https://raw.githubusercontent.com/daily-harvest/opportunities/master/web-1/data/ingredients.json')
ingredients_raw = ingredients_response.text
ingredients = json.loads(ingredients_raw)
