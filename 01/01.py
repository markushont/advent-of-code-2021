with open('input.txt', 'r') as f:
    data = f.readlines()
    lines = []
    for line in data:
        lines.append(int(line.strip()))

greater_indexes = []
tot = 0
for i in range(1, len(lines)):
    if lines[i-1] < lines[i]:
        tot = tot+1
        greater_indexes.append(i)
print(len(greater_indexes))
print(tot)
