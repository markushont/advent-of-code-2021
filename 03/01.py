data = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        for i in range(12):
            if len(data) < i+1:
                data.append([line[i]])
            else:
                data[i].append(line[i])

most_common_bin = ''
least_common_bin = ''

for col in data:
    most_common_bin += max(set(col), key=col.count)
    least_common_bin += min(set(col), key=col.count)

most_common = int(most_common_bin, 2)
least_commmon = int(least_common_bin, 2)
print(most_common*least_commmon)