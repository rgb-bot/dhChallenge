import unittest
from app import app
from app import *
from fetch import *
from search import *
from fetch import ingredients, products

class TestStringAlgo(unittest.TestCase):

  def test_correct_format(self):
    self.assertTrue(search_ingredients("Organic + Banana", ingredients, products)[0]["id"])
    self.assertTrue(search_ingredients("Organic + Banana", ingredients, products)[0]["name"])
    self.assertTrue(type(search_products([{"id": 65, "name": "Red Miso"}], products)), list)

  def test_basic_matching(self):
    self.assertEqual(type(search_ingredients("applee", ingredients, products)), list)
    self.assertTrue(type(create_output("bricks", ingredients, products)) == str)


class TestJSONs(unittest.TestCase):

  def test_json_retrieval(self):
    self.assertEqual(products_response.status_code, 200)
    self.assertEqual(ingredients_response.status_code, 200)

class FlaskTestCase(unittest.TestCase):

    def test_server(self):
      tester = app.test_client(self)
      response = tester.get("/search/search+term")
      self.assertEquals(response.status_code, 200)

    def test_server_content(self):
      tester = app.test_client(self)
      response = tester.get("/search/search+term")
      self.assertEquals(response.content_type, 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()