def greet(name: str, uppercase: bool = False) -> str:
    greeting = f"Hello, {name}!"
    return greeting.upper() if uppercase else greeting
