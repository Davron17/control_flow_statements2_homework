def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    largest=n%10
    if n//10000>n%10:
        largest=n//10000
    if (n-n//10000*10000)//1000>n%10:
        largest=(n-n//10000*10000)//1000
    if ((n-n//1000*1000)//100)>n%10:
        largest=(n-n//1000*1000)//100
    if (n-n//100*100)//10>n%10:
        largest=(n-n//100*100)//10
    return largest
print(main(50684))
print(main(12345))