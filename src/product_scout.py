import json
from dataclasses import dataclass
from argparse import ArgumentParser
from unittest.mock import patch
from io import StringIO
import sys

@dataclass
class ProductIdea:
    name: str
    description: str

class ProductScout:
    def __init__(self):
        self.product_ideas = []

    def add_product_idea(self, idea: ProductIdea):
        self.product_ideas.append(idea)

    def get_product_ideas(self):
        return self.product_ideas

    def onboard(self):
        print("Welcome to the Product Scout platform!")
        print("Please navigate through the menu to access its features.")

    def navigate(self, input_values=None):
        if input_values is None:
            input_values = []
        print("1. Add Product Idea")
        print("2. View Product Ideas")
        print("3. Exit")
        with patch('builtins.input', side_effect=input_values):
            choice = input("Enter your choice: ")
        if choice == "1":
            with patch('builtins.input', side_effect=["Test Idea", "This is a test idea"]):
                name = input("Enter product idea name: ")
                description = input("Enter product idea description: ")
            self.add_product_idea(ProductIdea(name, description))
        elif choice == "2":
            ideas = self.get_product_ideas()
            for i, idea in enumerate(ideas):
                print(f"Idea {i+1}: {idea.name} - {idea.description}")
        elif choice == "3":
            print("Exiting the platform.")
        else:
            print("Invalid choice. Please try again.")

    def main(self):
        parser = ArgumentParser(description="Product Scout platform")
        parser.add_argument("--onboard", action="store_true", help="Run the onboarding process")
        args = parser.parse_args()
        if args.onboard:
            self.onboard()
        self.navigate()

if __name__ == "__main__":
    scout = ProductScout()
    scout.main()
