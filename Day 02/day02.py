def verify(input):
    trend = [input[i]-input[i+1] for i in range(len(input)-1)]

    trend_direction = [y/abs(y) if y != 0 else 0 for y in trend]

    movement = [abs(y) for y in trend]

    return min(trend_direction) == max(trend_direction) and max(movement) <= 3 and min(movement) >= 1


input = [[int(y) for y in x.split(' ')] for x in open('Day 02/day02_input.txt').read().split('\n')]

# Task 1
output_1 = len([x for x in input if verify(x)])

# Task 2
output_2 = 0
for x in input:
    if verify(x):
        output_2 += 1
    else:
        for i in range(len(x)):
            x_edit = x.copy()
            x_edit.pop(i)

            if verify(x_edit):
                output_2 += 1
                break

print(output_2)