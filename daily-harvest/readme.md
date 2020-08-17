# Search Code Created For Daily Harvest

A RESTful implementation of a product search with an ingredient as a parameter

## Dependencies and Rquirements

Python 3 is required for this code.

Flask is the only dependency for this code:

```bash
pip install flask
```

## Usage

Run by executing the following line:

```bash
python3 fetch.py
```
Then in Postman, perform a request with the following:

```
GET http://127.0.0.1:5000/search/<search+term>
```
Note that spaces in the query should be separated by a "+" sign.

## Features

The search algorithm is very forgiving with typos. It also detects queries for fruits that don't exist in the database. For example, try searching for "Organci banas", or "watermln".


