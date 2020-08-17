from fetch import ingredients, products
from parse_tools import dice_coefficient


def searchIngredients(keywords):

  ingr_list = []

  ## clean data
  keywords = keywords.lower().strip().split("+")

  #remove organic for initial search
  organic = False
  if "organic" in keywords:
    organic = True
    keywords.remove("organic")

  keywords = " ".join(keywords)
  if len(keywords) == 0:
    return []


  #exact single word match
  for ingr in ingredients:
    if keywords in ingr["name"].lower():
      ingr_list.append({"id": ingr["id"], "name": ingr["name"]})

  #dice coefficient fuzzy match
  iterable_keywords = keywords.split()
  if len(ingr_list) == 0:
    for ingr in ingredients:
      for word in ingr["name"].split():
        for keyword in iterable_keywords:
          # checks similarity of word for word, then similarity of entire phrase
          if dice_coefficient(word.lower(), keyword) > .8 or dice_coefficient(ingr["name"], keywords) < - 0.6:
            ingr_list.append({"id": ingr["id"], "name": ingr["name"]})
            continue

  if organic and ("Organic" in ingr_list):
    for item in ingr_list:
      if "Organic" not in item:
        ingr_list.remove(item)

  return ingr_list


def searchProducts(input):
  prod_list = []
  for item in input:
    for product in products:
      if item["id"] in product["ingredientIds"]:
        prod_list.append(product["name"])
  if len(prod_list) == 0:
    return "Not Found"
  else:
    return prod_list


# print(searchIngredients("Organic+Banana"))
# print(searchProducts([{'id': 81, 'name': 'Organic Banana'}]))


