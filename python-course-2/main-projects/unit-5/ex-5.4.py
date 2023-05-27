def check_id_valid(id_number):
    """
    Check if an ID number is valid.

    Args:
        id_number (int): The ID number to be checked.

    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    sum = 0
    even = False
    if len(str(id_number)) != 9:
        return False
    for digit in str(id_number):
        digit = int(digit)
        if even:
            sum += ((digit * 2) // 10) + ((digit * 2) % 10)
        else:
            sum += digit
        even = (not even)
    return sum % 10 == 0


class IDIterator:
    """
    Iterator for generating valid ID numbers starting from a given number.

    Args:
        id (int): The starting ID number.

    Methods:
        __iter__(): Returns the iterator object itself.
        __next__(): Returns the next valid ID number.

    Raises:
        StopIteration: When there are no more valid ID numbers to generate.
    """
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        number = self._id + 1
        while number <= 999999999:
            if check_id_valid(number):
                self._id = number
                return number
            number += 1
        raise StopIteration


def id_generator(id_number):
    """
    Generator for generating valid ID numbers starting from a given number.

    Args:
        id_number (int): The starting ID number.

    Yields:
        int: The next valid ID number.
    """
    new_id = id_number + 1
    while new_id <= 999999999:
        if check_id_valid(new_id):
            yield new_id
        new_id += 1


def main():
    """
    Main function for user interaction.
    """
    id_number = int(input("Enter ID: "))
    it_gen = input("Enter \"gen\" or \"it\": ")
    if it_gen == "it":
        iterator = iter(IDIterator(id_number))
        for i in range(10):
            new_id = next(iterator)
            print(new_id)
    else:
        generator = id_generator(id_number)
        for i in range(10):
            new_id = next(generator)
            print(new_id)


if __name__ == '__main__':
    main()
