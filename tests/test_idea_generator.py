from idea_generator import IdeaGenerator, Idea
import pytest

@pytest.fixture
def idea_generator():
    return IdeaGenerator()

def test_get_ideas(idea_generator):
    ideas = idea_generator.get_ideas()
    assert len(ideas) == 5

def test_get_ideas_with_category(idea_generator):
    ideas = idea_generator.get_ideas("tech")
    assert len(ideas) == 2
    for idea in ideas:
        assert idea.category == "tech"

def test_filter_ideas(idea_generator):
    ideas = idea_generator.filter_ideas("marketing")
    assert len(ideas) == 2
    for idea in ideas:
        assert idea.category == "marketing"

def test_filter_ideas_with_invalid_category(idea_generator):
    ideas = idea_generator.filter_ideas("invalid")
    assert len(ideas) == 0

def test_get_ideas_with_none_category(idea_generator):
    ideas = idea_generator.get_ideas(None)
    assert len(ideas) == 5
