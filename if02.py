def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<(b and c):
        return a
    if b<(a and c):
        return b
    if c<(a and b):
        return c
print(main(1,2,3))
print(main(5,6,8))
    