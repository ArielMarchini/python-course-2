import functools


def add_digit(total, digit):
    return int(total) + int(digit)


def sum_of_digits(number):
    return functools.reduce(add_digit, list(str(number)))

