from fetch import ingredients, products
from parse_tools import dice_coefficient


def search_ingredients(query_string, ingr_source, products_source):
  '''Retrieves ingredients that match the keyword.
  Args:
    keywords: User search query string.

  Returns:
    An array of dicts representing each ingredient. For example:
    [
      {"id": 81,
      "name": "Organic Bananas"
      }
    ]

  '''

  ingr_list = []


  ## clean data
  keywords_temp = query_string.lower().strip().split("+")

  #remove organic for initial search
  organic = False
  if "organic" in keywords_temp:
    organic = True
    keywords_temp.remove("organic")

  query_string = " ".join(keywords_temp)

  if len(query_string) == 0:
    return [{}]


  #exact single word match
  for ingr in ingr_source:
    menu_name = ingr["name"].lower()
    # detects errant partial matches.
    # For example, "peas" has an exact match in "peanuts", but it should not match with "Organic Peanut Butter"
    if query_string in menu_name and (dice_coefficient(menu_name, query_string) > 0.6 or dice_coefficient(menu_name, query_string) < -0.5):
      ingr_list.append({"id": ingr["id"], "name": ingr["name"]})

  #dice coefficient fuzzy match
  if len(query_string) > 3:
    keywords = query_string.split()
    if len(ingr_list) == 0:
      for ingr in ingr_source:
        for word in ingr["name"].split():
          for keyword in keywords:
            # checks similarity of word for word, then similarity of entire phrase
            if (dice_coefficient(word.lower(), keyword) > .8 or dice_coefficient(word.lower(), keyword) < -0.6):
              ingr_list.append({"id": ingr["id"], "name": ingr["name"]})
              continue

    if organic and ("Organic" in ingr_list):
      for item in ingr_list:
        if "Organic" not in item:
          ingr_list.remove(item)

  return ingr_list


def search_products(input, products_source):
  prod_list = []
  for item in input:
    for product in products_source:
      if item["id"] in product["ingredientIds"]:
        prod_list.append(product["name"])
  if len(prod_list) == 0:
    return "Not Found"
  else:
    return prod_list



