def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    x1 = s[0]
    x2 = s[-1]
    return x1 + x2
print(main("code"))