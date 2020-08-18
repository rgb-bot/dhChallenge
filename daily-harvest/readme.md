# Search Code Created For Daily Harvest

A RESTful implementation of a product search with an ingredient as a parameter

## String Matching Algorithm

I have implemented a custom version of the Dice Coefficient to interpret typos. The search algorithm is fairly robust, and handles many types of user input typos. For example, try searching for "organic+shrooms", "berry", "aracola", and " bbananas".

## Output Format

If there is no match, the code sends a "No matches found" response:
```
Example: {"products": [],
          "error": "Oops! No matching ingredients found."}
```
If there are multiple matches, the code sends a list of possible ingredient matches and instructs the user to search again:
```
Example: {"products": [],
          "ingredient_searched": null,
          "error": "There are multiple matches for your search. Try searching again
                   with: Organic Apple, Organic Apple Cider Vinegar"}
```
Else, the code sends a list of products that contain that ingredient.
```
Example: {"products": ["Mango + Papaya", "Pineapple + Matcha", "Mango + Turmeric"],
          "ingredient_searched": "Organic Pineapple",
          "error": null}
```
## Dependencies and Rquirements

Python 3 is required for this code.

Flask is the only dependency for this code:

```bash
pip install flask
```

## Usage

Run by executing the following line:

```bash
python3 app.py

```
Then in Postman, perform a request with the following:

```
GET http://127.0.0.1:5000/search/<search+term>
```
Note that spaces in the query should be separated by a "+" sign.


