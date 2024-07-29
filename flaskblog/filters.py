def safe_truncate(text, max_length=250, suffix="..."):
    """
    Truncate the text at the end of the nearest word if it exceeds max_length.
    """
    if len(text) <= max_length:
        return text

    truncated = text[:max_length].rsplit(" ", 1)[0]
    return f"{truncated}{suffix}"


