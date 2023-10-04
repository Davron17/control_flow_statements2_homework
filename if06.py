def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    largest=n%10
    index=1
    if n//10000>n%10:
        largest=n//10000
        index=5
    if (n-n//10000*10000)//1000>n%10:
        largest=(n-n//10000*10000)//1000
        index=4
    if ((n-n//1000*1000)//100)>n%10:
        largest=(n-n//1000*1000)//100
        index=3
    if (n-n//100*100)//10>n%10:
        largest=(n-n//100*100)//10
        index=2
    return largest,index
print(main(50684))
print(main(12345))
    