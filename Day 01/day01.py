input = [[int(y) for y in x.split(' ') if y != ''] for x in open('Day 01/day01_input.txt').read().split('\n')]

list_1 = [x[0] for x in input]
list_2 = [x[1] for x in input]

list_1.sort()
list_2.sort()

# Task 1
output_1 = sum([abs(x[0] - x[1]) for x in list(zip(list_1, list_2))])

# Task 2
output_2 = sum([len([y for y in list_2 if x==y])*x for x in list_1])
print(output_2)