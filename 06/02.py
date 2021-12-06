with open('input.txt', 'r') as f:
    init_fish = [int(x) for x in f.readlines()[0].strip().split(',')]

fish = {i: 0 for i in range(9)}
for f in init_fish:
    fish[f-1] += 1

for i in range(255):
    orig = {k:v for k,v in fish.items()}
    expired = orig[0]
    for j in reversed(range(7)):
        fish[(j-1)%7] = orig[j]
    fish[6] += orig[7]
    fish[7] = orig[8]
    fish[8] = expired

print(sum(fish.values()))