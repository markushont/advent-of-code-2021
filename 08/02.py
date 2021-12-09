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

#d0 - The one found in #7 but not in #1
#d1 - The one found in #9 but not in #3
#d2 - The one found in #8 but not in #6
#d3 - The one found in #8 but not in #0
#d4 - The one found in #8 but not in #9
#d5 - The one found in #1 but not in #2
#d6 - Not d0, d2, d3, d4 in #2


#1 - len() == 2
#2 - Last remaining
#3 - All in 9 except one
#4 - len() == 4
#5 - All in #6 except one
#6 - All except one of #1
#7 - len() == 3
#8 - len() == 7
#9 - All in 4 and in 1 and one more

#1 - len() == 2
#4 - len() == 4
#7 - len() == 3
#8 - len() == 7
#9 - All in #4 and in #1 and one more
#3 - All in #9 except one
#6 - All except one of #1
#5 - All in #6 except one
#2 - Last remaining

def compare(sub, string):
    for char in sub:
        if char not in string:
            return False

    return True

res = 0
for i in range(len(inputs)):
    input = [''.join(sorted(x)) for x in inputs[i]]
    # input = [''.join(sorted(x)) for x in ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']]
    one = next(x for x in input if len(x) == 2)
    four = next(x for x in input if len(x) == 4)
    seven = next(x for x in input if len(x) == 3)
    eight = next(x for x in input if len(x) == 7)
    nine = next(x for x in input if len(x) == 6 and compare(one, x) and compare(four, x))
    three = next(x for x in input if len(x) == 5 and compare(x, nine) and compare(one, x))
    six = next(x for x in input if len(x) == 6 and (one[0] in x or one[1] in x) and not (one[0] in x and one[1] in x))
    five = next(x for x in input if len(x) == 5 and compare(x, six) and x != three)
    zero = next(x for x in input if len(x) == 6 and x not in [nine, six])
    two = next(x for x in input if x not in [zero, one, three, four, five, six, seven, eight, nine])
    transformers = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine
    }
    output_number = ''
    outputs_sorted = [''.join(sorted(outp)) for outp in outputs[i]] 
    # outputs_sorted = [''.join(sorted(outp)) for outp in ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf']] 
    for j in range(len(outputs_sorted)):
        output = outputs_sorted[j]
        for num, val in transformers.items():
            if output == val:
                output_number += str(num)
                break
    # if len(output_number) != 4:
    #     res += int(output_number)
    #     break
    # print(input, transformers, output_number, int(output_number), [''.join(sorted(outp)) for outp in outputs[i]])
    res += int(output_number)

print(res)


