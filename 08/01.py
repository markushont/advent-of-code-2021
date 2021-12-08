with open('input.txt', 'r') as f:
    input = []
    output = []
    for line in f.readlines():
        [i, o] = line.strip().split(' | ')
        input.append(i.split())
        output.append(o.split())

flat_out = [o for line in output for o in line]

count = 0
for o in flat_out:
    if len(o) in (2, 3, 4, 7):
        count += 1

print(count)