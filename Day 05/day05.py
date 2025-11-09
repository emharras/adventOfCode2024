
input = open('Day 05/day05_input.txt').read().split('\n\n')

rules = [x.split('|') for x in input[0].split('\n')]
rules = {x: [z[0] for z in rules if x ==z[1]] for x in list(set([y[1] for y in rules]))}

manuals = [x.split(',') for x in input[1].split('\n')]

output_1 = []
invalid_manuals = []
for row in manuals:
    count = 0
    for i in range(len(row)):
        i_rule = rules.get(row[i], [])

        row_violation = [x for x in row[i:] if x in i_rule]
        if len(row_violation) > 0:
            count += 1
            break

    if count == 0:
        output_1.append(int(row[len(row)//2]))
    else:
        invalid_manuals.append(row)

output_1 = sum(output_1)


output_2 = []
for row in invalid_manuals:
    row_copy = row.copy()
    while True:
        count = 0
        for i in range(len(row_copy)):
            i_rule = rules.get(row_copy[i], [])
            row_violation = [x for x in row_copy[i:] if x in i_rule]

            if len(row_violation) > 0:
                violation_index = max([row_copy.index(x) for x in row_violation])
                row_copy.append(row_copy[i])
                row_copy.pop(i)
                count += 1
                break
        
        if count == 0:
            output_2.append(int(row_copy[len(row_copy)//2]))
            break

output_2 = sum(output_2)
print(output_2)