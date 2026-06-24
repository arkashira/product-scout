from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Idea:
    id: int
    category: str
    description: str

class IdeaGenerator:
    def __init__(self):
        self.ideas = [
            Idea(1, "tech", "AI-powered chatbot"),
            Idea(2, "tech", "Virtual reality platform"),
            Idea(3, "marketing", "Social media management tool"),
            Idea(4, "marketing", "Influencer marketing platform"),
            Idea(5, "finance", "Cryptocurrency trading platform"),
        ]

    def get_ideas(self, category: str = None) -> List[Idea]:
        if category:
            return [idea for idea in self.ideas if idea.category == category]
        return self.ideas

    def filter_ideas(self, category: str) -> List[Idea]:
        return self.get_ideas(category)
