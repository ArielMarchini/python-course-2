def divisible_by_4(num):
    if num % 4 == 0:
        return True

def four_dividers(number):
    return list(filter(divisible_by_4, range(1, number + 1)))

