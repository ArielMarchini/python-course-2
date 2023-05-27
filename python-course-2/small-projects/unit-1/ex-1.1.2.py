import functools

def add_last_letter(str, letter):
    return str + ("".join(letter) * 2)

def double_letter(my_str):
    return my_str[0] + "".join(functools.reduce(add_last_letter, list(my_str)))
