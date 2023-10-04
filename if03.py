def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max=a
    small=a
    if max<b:
        max=b
    if max<c:
        max=c
    if small>b:
        small=b
    if small>c:
        small=c
    return a+b+c-small-max
print(main(5,6,3))
print(main(4,9,78))