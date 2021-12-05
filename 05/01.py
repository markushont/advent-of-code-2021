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
    x_0 = min(line[0][0], line[1][0])
    x_1 = max(line[0][0], line[1][0])
    y_0 = min(line[0][1], line[1][1])
    y_1 = max(line[0][1], line[1][1])

    if x_0 == x_1:
        for i in range(y_0, y_1+1):
            matrix[x_0][i] += 1
    elif y_0 == y_1:
        for i in range(x_0, x_1+1):
            matrix[i][y_0] += 1

points = 0
for x, y_vals in matrix.items():
    for y, val in y_vals.items():
        if val > 1:
            points += 1

print(points)
