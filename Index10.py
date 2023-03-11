def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    y1 = int(s[0])
    y2 = int(s[1])
    y3 = int(s[2])
    y4 = int(s[3])
    y5 = int(s[4])
    a = y1+y2+y3+y4+y5
    return a
print(main("22345"))