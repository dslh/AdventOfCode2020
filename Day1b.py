from itertools import combinations
#from get_aoc import get_input_integers
#expenses = get_input_integers(1)

#Data from Advent of Code Day1 2020

from get_aoc import get_input_lines

split_input = get_input_lines(1)
print("split_input = ")
print(split_input)
print(type(split_input))

expenses = [int(string) for string in split_input]
print("expenses = ")
print(expenses)
print(type(expenses))

all_expense_pairs = list(combinations(expenses, 3))
print("all expense pairs = ")
print(all_expense_pairs)
print(type(all_expense_pairs))

#testi = 1

def sums_to_2020(values):
    #print(testi)
    #testi = testi + 1
    print("hello")
    return sum (values) == 2020

result = list(filter(sums_to_2020, all_expense_pairs))
print(result)
#x, y = result(0)
#print(result)
#print(x * y)