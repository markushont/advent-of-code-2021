with open('input.txt', 'r') as f:
    instructions = [
        (line.strip().split()[0], int(line.strip().split()[1]))
        for line in f.readlines()
    ]

depth = 0
distance = 0
aim = 0
for instr in instructions:
    if instr[0] == 'forward':
        distance += instr[1]
        depth += instr[1] * aim
    elif instr[0] == 'up':
        aim -= instr[1]
    elif instr[0] == 'down':
        aim += instr[1]

print(depth, distance, depth*distance)