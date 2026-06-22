def sanitize(text: str, uppercase: bool = False) -> str:
    sanitized = text.strip()
    return sanitized.upper() if uppercase else sanitized
