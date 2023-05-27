from itertools import combinations

bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
combinations_list = []
for r in range(1, len(bills) + 1):
    combinations_list.extend(combinations(bills, r))
valid_combinations = [comb for comb in combinations_list if sum(comb) == 100]
unique_combinations = set(valid_combinations)
for comb in unique_combinations:
    print(comb)