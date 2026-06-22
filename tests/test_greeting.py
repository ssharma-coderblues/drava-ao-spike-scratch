from src.greeting import greet

def test_greet_basic():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_world():
    assert greet("World") == "Hello, World!"


def test_greet_uppercase():
    assert greet("Alice", uppercase=True) == "HELLO, ALICE!"
