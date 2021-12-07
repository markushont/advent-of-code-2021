with open('input.txt', 'r') as f:
    positions = sorted([int(x) for x in f.readlines()[0].strip().split(',')])
n_positions = len(positions)

if int(n_positions/2) != n_positions/2:
    median = positions[n_positions / 2]
else:
    median = (positions[int(n_positions/2)] + positions[int(n_positions/2) + 1])/2

fuel_spend = sum([abs(x-median) for x in positions])

print(median, fuel_spend)