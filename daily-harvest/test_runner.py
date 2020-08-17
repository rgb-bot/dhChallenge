import unittest
from server import app
from fetch import *
from search import *
from main import *

class TestStringMatching(unittest.TestCase):

  def test_has_correct_keys(self):
    self.assertTrue(searchIngredients("Organic + Banana")[0]["id"])
    self.assertTrue(searchIngredients("Organic + Banana")[0]["name"])

  def test_basic_matching(self):
    self.assertEqual(type(searchIngredients("applee")), list)
    self.assertTrue(type(createOutput("bricks")) == str )


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