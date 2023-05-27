def shift_up(string):
    return ''.join(chr(ord(char) + 2) if (char.isalpha() or char.isdigit()) else char for char in string)

