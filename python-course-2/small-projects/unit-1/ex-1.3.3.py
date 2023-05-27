import functools

def is_funny(string):
    return bool(functools.reduce(lambda state, new: state * new, [True if (char == 'h' or char == 'a') else False for char in string]))
