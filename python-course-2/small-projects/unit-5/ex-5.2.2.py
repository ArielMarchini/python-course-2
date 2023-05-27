numbers = iter(list(range(1, 101)))

for i in numbers:
    try:
        print(i)
        next(numbers)
        next(numbers)
    except:
        pass
