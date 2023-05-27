file_content = open('names.txt', 'r').read().split('\n')

# 1. Find the name with the maximum length:
print(max([name for name in file_content], key=len))

# 2. Calculate the sum of all name lengths:
print(sum([len(name) for name in file_content]))

# 3. Find and print the name(s) with the minimum length:
min_len = len(min([name for name in file_content], key=len))
names_min = list(filter(lambda name: len(name) == min_len, [name for name in file_content]))
[print(name) for name in names_min]

# 4. Write the lengths of all names to a file:
file = open('name_length.txt', 'w')
[file.write(str(len(single_name)) + '\n') for single_name in file_content]
file.close()

# 5. Find and print the names with a specific length:
number = int(input("Enter number: "))
names_valid = list(filter(lambda name: len(name) == number, [name for name in file_content]))
[print(name) for name in names_valid]