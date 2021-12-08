with open('input.txt', 'r') as f:
    inputs = []
    outputs = []
    for line in f.readlines():
        [i, o] = line.strip().split(' | ')
        inputs.append(i.split())
        outputs.append(o.split())

#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

digits = {
    0: (0, 1, 2, 4, 5, 6),
    1: (2, 5),
    2: (0, 2, 3, 4, 6),
    3: (0, 2, 3, 5, 6),
    4: (1, 2, 3, 5),
    5: (0, 1, 3, 5, 6),
    6: (0, 1, 3, 4, 5, 6),
    7: (0, 2, 5),
    8: (0, 1, 2, 3, 4, 5, 6),
    9: (0, 1, 2, 3, 5, 6)
}

#Well-known: 1, 4, 7, 8

#d0 - The one found in #7 but not in #1
#d1 - The one found in #9 but not in #3
#d2 - The one found in #8 but not in #6
#d3 - The one found in #8 but not in #0
#d4 - The one found in #8 but not in #9
#d5 - The one found in #1 but not in #2
#d6 - Not d0, d2, d3, d4 in #2

input = inputs[0]

one = next(x for x in input if len(x) == 2)


