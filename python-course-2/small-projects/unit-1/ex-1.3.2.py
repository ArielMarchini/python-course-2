def is_prime(number):
    return bool([True for num in range(2, number) if number % num == 0])

