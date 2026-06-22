from src.utils import sanitize


def bid_farewell(name: str, uppercase: bool = False) -> str:
    sanitized_name = sanitize(name)
    farewell = f"Goodbye, {sanitized_name}!"
    return farewell.upper() if uppercase else farewell
