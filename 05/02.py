data = []
with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        points = line.split(' -> ')
        line_data = []
        for point in points:
            coords = point.split(',')
            line_data.append([int(coords[0]), int(coords[1])])
        data.append(line_data)

max_x = 0
max_y = 0
for line in data:
    if line[0][0] > max_x:
        max_x = line[0][0]
    if line[1][0] > max_x:
        max_x = line[1][0]
    if line[0][1] > max_y:
        max_y = line[0][1]
    if line[1][1] > max_y:
        max_y = line[1][1]

matrix = {x: {y: 0 for y in range(0, max_y+1)} for x in range(0, max_x+1)}

for line in data:
    x_0 = line[0][0]
    x_1 = line[1][0]
    y_0 = line[0][1]
    y_1 = line[1][1]

    if x_0 == x_1:
        for i in range(min(y_0, y_1), max(y_0, y_1)+1):
            matrix[x_0][i] += 1
    elif y_0 == y_1:
        for i in range(min(x_0, x_1), max(x_0, x_1)+1):
            matrix[i][y_0] += 1
    else:
        dx = 1 if x_1 > x_0 else -1
        dy = 1 if y_1 > y_0 else -1
        for i in range(abs(y_1 - y_0)+1):
            matrix[x_0 + dx*i][y_0 + dy*i] += 1

points = 0
for x, y_vals in matrix.items():
    for y, val in y_vals.items():
        if val > 1:
            points += 1

print(points)
