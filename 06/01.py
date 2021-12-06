with open('input.txt', 'r') as f:
    init_fish = [int(x) for x in f.readlines()[0].strip().split(',')]

fish = init_fish
for i in range(80):
    expired = fish.count(0)
    newborns = [x-1 for x in fish if x >= 7]
    fish = [(x - 1)%7 for x in fish if x < 7]
    fish.extend(newborns)
    fish.extend([8] * expired)

print(len(fish))