from fetch import *

def searchProducts(ingredient_id):
  for item in products:
    if ingredient_id in item["ingredientIds"]:
      print(item["name"])

# searchProducts(190)


def searchIngredients(keywords):
  for ingr in ingredients:
    if keywords in ingr["name"]:
      print(ingr["name"])

searchIngredients("Almond Butter")