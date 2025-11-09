import re

def mul(input):
    mul_re = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    return sum([int(x[0])*int(x[1]) for x in re.findall(mul_re, input)])


input = open('Day 03/day03_input.txt').read()

# Task 1
output_1 = mul(input)

# Task 2
while "don't()" in input:
    i = input.find("don't()")
    for j in re.finditer(r'(do\(\))', input):
        if i < j.start(0):
            input = input[0:i] + input[j.start(0):]
            break

output_2 = mul(input)
print(output_2)