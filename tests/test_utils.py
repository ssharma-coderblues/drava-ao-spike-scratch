from src.utils import sanitize

def test_sanitize_strips_whitespace():
    assert sanitize("  hello  ") == "hello"

def test_sanitize_no_change():
    assert sanitize("clean") == "clean"

def test_sanitize_inner_spaces():
    assert sanitize("  hello world  ") == "hello world"
