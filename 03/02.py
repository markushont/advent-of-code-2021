
data = []
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    # lines = ['110', '010']
    data_d = {i: lines[i] for i in range(len(lines))}
    for line in lines:
        for i in range(len(line)):
            if i >= len(data):
                data.append([line[i]])
            else:
                data[i].append(line[i])


ox_gen = {k: v for k, v in data_d.items()}
for bitno in range(len(lines[0])):
    data_c = [data[bitno][i] for i in ox_gen.keys()]
    count_one = data_c.count('1')
    count_zero = data_c.count('0')
    most_common = '1' if count_one >= count_zero else '0'
    print('most_common: ', most_common, 'bitno: ', bitno, 'count_one: ', count_one, 'count_zero: ', count_zero)
    for i in range(len(lines)):
        if len(ox_gen.keys()) == 1:
            break
        if i in ox_gen and ox_gen[i][bitno] != most_common:
            ox_gen.pop(i, None)
    if len(ox_gen.keys()) == 1:
        break

scrub_rat = {k: v for k, v in data_d.items()}
for bitno in range(len(lines[0])):
    data_c = [data[bitno][i] for i in scrub_rat.keys()]
    count_one = data_c.count('1')
    count_zero = data_c.count('0')
    least_common = '0' if count_zero <= count_one else '1'
    print('most_common: ', most_common, 'bitno: ', bitno, 'count_one: ', count_one, 'count_zero: ', count_zero)
    for i in range(len(lines)):
        if len(scrub_rat.keys()) == 1:
            break
        if i in scrub_rat and scrub_rat[i][bitno] != least_common:
            scrub_rat.pop(i, None)
    if len(scrub_rat.keys()) == 1:
        break

# print(scrub_rat)
print(ox_gen, scrub_rat)

print(int(list(ox_gen.values())[0], 2) * int(list(scrub_rat.values())[0], 2))