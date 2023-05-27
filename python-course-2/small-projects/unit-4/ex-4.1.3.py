import sys


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def first_prime_over(n):
    print(next(number for number in range(n + 1, sys.maxsize) if is_prime(number)))


first_prime_over(1000)