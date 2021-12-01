with open('input.txt', 'r') as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(sum([1 for i in range(3, len(lines)) if lines[i] > lines[i-3]]))

# head = -1
# tail = -1
# n_increases = 0
# for i in range(3, len(lines)):
#     head = lines[i]
#     tail = lines[i-3]

#     if head > tail:
#         n_increases += 1

# for i in range(3, len(lines)):
#     n_increases += 1 if lines[i] > lines[i-3] else 0
# print(n_increases)