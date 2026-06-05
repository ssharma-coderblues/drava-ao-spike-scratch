from src.farewell import bid_farewell

def test_bid_farewell_basic():
    assert bid_farewell("Alice") == "Goodbye, Alice!"

def test_bid_farewell_world():
    assert bid_farewell("World") == "Goodbye, World!"
