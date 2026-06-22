def bid_farewell(name: str, uppercase: bool = False) -> str:
    farewell = f"Goodbye, {name}!"
    return farewell.upper() if uppercase else farewell
