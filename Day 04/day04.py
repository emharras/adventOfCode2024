import re

def horizontal(input):
    return sum([len(re.findall(r'X(?=MAS)', x)) + len(re.findall(r'S(?=AMX)', x)) for x in input])

def vertical_test(input, i, j, up=True):
    if up:
        if i < 3:
            return 0
        else:
            i_dir = -1
    else:
        i_dir = 1

    try:
        if input[i+(1*i_dir)][j] == 'M' and input[i+(2*i_dir)][j] == 'A' and input[i+(3*i_dir)][j] == 'S':
            return 1
        else:
            return 0
    except IndexError:
        return 0

def vertical(input):
    count = 0
    for i in range(len(input)):
        for x in re.finditer('X', input[i]):
            count += vertical_test(input, i, x.start(0))
            count += vertical_test(input, i, x.start(0), up=False)
    return count

def diagonal_test(input, i, j, up=True, forward = True):
    if up:
        if i < 3:
            return 0
        else:
            i_dir = -1
    else:
        i_dir = 1
    
    if forward:
        j_dir = 1
    else:
        if j < 3:
            return 0
        else:
            j_dir = -1

    try:
        if input[i+(1*i_dir)][j+(1*j_dir)] == 'M' and input[i+(2*i_dir)][j+(2*j_dir)] == 'A' and input[i+(3*i_dir)][j+(3*j_dir)] == 'S':
            return 1
        else:
            return 0
    except IndexError:
        return 0

def diagonal(input):

    count = 0
    for i in range(len(input)):
        for x in re.finditer('X', input[i]):
            count += diagonal_test(input, i, x.start(0))
            count += diagonal_test(input, i, x.start(0), up=False)
            count += diagonal_test(input, i, x.start(0), forward=False)
            count += diagonal_test(input, i, x.start(0), up=False, forward=False)

    return count

def xmas_test(input, i, j):
    if 0 == i or 0 == j:
        return 0
    
    try:
        cross_1 = [input[i+1][j+1], input[i-1][j-1]]
        cross_2 = [input[i+1][j-1], input[i-1][j+1]]
        cross_1.sort()
        cross_2.sort()
        if cross_1 == ['M', 'S'] and cross_1 == cross_2:
            return 1
        else:
            return 0
    except IndexError:
        return 0


input = open('Day 04/day04_input.txt').read()

input = input.split('\n')

# Task 1
output_1 = horizontal(input) + vertical(input) + diagonal(input)

# Task 2
output_2 = sum([sum([xmas_test(input, i, a.start(0)) for a in re.finditer('A', input[i])]) for i in range(len(input))])
print(output_2)
