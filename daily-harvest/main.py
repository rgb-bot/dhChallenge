from search import *

def createOutput(input):
  ingredients = searchIngredients(input)
  if len(ingredients) == 0:
    return "Oops! No matches found."
  elif len(ingredients) == 1:
    products = searchProducts(ingredients)
    return "The following contain " + ingredients[0]["name"] + ": " + "\n \n" + ", ".join(products)
  else:
    array = []
    for item in ingredients:
        array.append(item["name"])
    return "There are multiple matches for your search. Try searching again with: \n \n" + ", ".join(array)




# print(createOutput("organic+banana"))



