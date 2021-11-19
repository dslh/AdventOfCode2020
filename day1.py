#!/usr/bin/env python3

from itertools import combinations
from get_aoc import get_input_integers

expenses = get_input_integers(1)

all_expense_pairs = list(combinations(expenses, 2))
def sums_to_2020(values):
    return sum(values) == 2020

result = list(filter(sums_to_2020, all_expense_pairs))
x, y = result[0]
print(result)
print(x * y)
