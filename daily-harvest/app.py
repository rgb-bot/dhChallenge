from flask import Flask
from search import *
import json
from fetch import ingredients, products


def create_output(query_string, ingr_source, products_source):
    '''Returns a reponse JSON that contains the results of user search.

    Args:
        query_string: user search query string
    Returns:
        A JSON with a list of products or an error message. For example,
        {
            "products": ["Coconut + Water", “Chocolate + Blueberry”, “Ginger + Greens”],
            "ingredient_searched":
            "error": None
        }
        '''

    returned_ingr = search_ingredients(query_string, ingr_source, products_source)
    returned_products = search_products(returned_ingr, products_source)

    if len(returned_ingr) == 0:
        return json.dumps({
            "products": [],
            "error": "Oops! No matching ingredients found."
        })
    elif len(returned_ingr) == 1:
        # for cases in which ingr exists but no product with that ingredient
        if returned_products[0] == None:
            return json.dumps({
                "products": [],
                "ingredient_searched": returned_ingr[0]["name"],
                "error": None
            })

        #otherwise, return list of matching products
        return json.dumps({
            "products": returned_products,
            "ingredient_searched": returned_ingr[0]["name"],
            "error": None
        })
    else:
        products_list = []
        for item in returned_ingr:
            products_list.append(item["name"])
        # return "There are multiple matches for your search. Try searching again with: \n \n" + ", ".join(array)
        return json.dumps({
            "products": [],
            "ingredient_searched": None,
            "error": "There are multiple matches for your search. Try searching again with: " + ", ".join(products_list)
        })

app = Flask(__name__)
@app.route('/search/<query>')
def home(query):
    return create_output(query, ingredients, products)
if __name__ == '__main__':
    app.run(debug=True)