from flask import Flask
from search import *


def create_output(input):
    '''Creates response JSONs.

    Args:
        input: user search query string
    Returns:
        A JSON with a list of products or an error message. For example,
        {
            "products": ["Coconut + Water", “Chocolate + Blueberry”, “Ginger + Greens”],
            "error": None
        }
        '''

    ingredients = search_ingredients(input)

    if len(ingredients) == 0:
        return "Oops! No matches found."
    elif len(ingredients) == 1:
        products = search_products(ingredients)
        return "The following contain " + ingredients[0]["name"] + ": " + "\n \n" + ", ".join(products)
    else:
        array = []
        for item in ingredients:
            array.append(item["name"])
        return "There are multiple matches for your search. Try searching again with: \n \n" + ", ".join(array)

app = Flask(__name__)
@app.route('/search/<query>')
def home(query):
    return create_output(query)
if __name__ == '__main__':
    app.run(debug=True)