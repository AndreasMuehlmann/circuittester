def left_pad(string: str, char: str, length: int):
    if len(string) >= length:
        return string
    return char * (length - len(string)) + string
