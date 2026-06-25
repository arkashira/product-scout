from product_scout import ProductScout, ProductIdea
import io
import sys
import unittest
from unittest.mock import patch

class TestProductScout(unittest.TestCase):

    def test_add_product_idea(self):
        scout = ProductScout()
        idea = ProductIdea("Test Idea", "This is a test idea")
        scout.add_product_idea(idea)
        self.assertEqual(len(scout.get_product_ideas()), 1)
        self.assertEqual(scout.get_product_ideas()[0].name, "Test Idea")
        self.assertEqual(scout.get_product_ideas()[0].description, "This is a test idea")

    def test_get_product_ideas(self):
        scout = ProductScout()
        idea1 = ProductIdea("Idea 1", "Description 1")
        idea2 = ProductIdea("Idea 2", "Description 2")
        scout.add_product_idea(idea1)
        scout.add_product_idea(idea2)
        ideas = scout.get_product_ideas()
        self.assertEqual(len(ideas), 2)
        self.assertEqual(ideas[0].name, "Idea 1")
        self.assertEqual(ideas[0].description, "Description 1")
        self.assertEqual(ideas[1].name, "Idea 2")
        self.assertEqual(ideas[1].description, "Description 2")

    def test_onboard(self):
        scout = ProductScout()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        scout.onboard()
        sys.stdout = sys.__stdout__
        self.assertIn("Welcome to the Product Scout platform!", capturedOutput.getvalue())

    def test_navigate(self):
        scout = ProductScout()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        scout.navigate(["1", "Test Idea", "This is a test idea"])
        sys.stdout = sys.__stdout__
        self.assertIn("1. Add Product Idea", capturedOutput.getvalue())
        self.assertIn("2. View Product Ideas", capturedOutput.getvalue())
        self.assertIn("3. Exit", capturedOutput.getvalue())

if __name__ == "__main__":
    unittest.main()
