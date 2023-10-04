def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    number=a
    if a<b:
        number=b
    if a==b:
        number=0    
    return number
print(main(1,1))
print(main(1,2))