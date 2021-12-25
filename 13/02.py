with open('input.txt', 'r') as f:
    dots = []
    folds = []
    for line in f.readlines():
        line = line.strip()
        if ',' in line:
            dots.append(
                (int(line.split(',')[0]), int(line.split(',')[1]))
            )
        elif '=' in line:
            folds.append(
                (line.split('=')[0].strip('fold along '), int(line.split('=')[1]))
            )

old_dots = {dot for dot in dots}
for fold in folds:
    new_dots = set()
    for dot in old_dots:
        if fold[0] == 'y' and dot[1] > fold[1]:
            new_dot = (dot[0], 2*fold[1] - dot[1])
        elif fold[0] == 'x' and dot[0] > fold[1]:
            new_dot = (2*fold[1] - dot[0], dot[1])
        else:
            new_dot = (dot[0], dot[1])

        new_dots.add(new_dot)
    old_dots = {dot for dot in new_dots}

dots = {}
for dot in old_dots:
    if dot[0] not in dots:
        dots[dot[0]] = {dot[1]: True}
    else:
        dots[dot[0]][dot[1]] = True


max_x = 0
max_y = 0

for dot in old_dots:
    if dot[0] > max_x:
        max_x = dot[0]
    if dot[1] > max_y:
        max_y = dot[1]


lines = []
for y in range(max_y+1):
    line = []
    for x in range(max_x+1):
        if x in dots and y in dots[x]:
            line.append('#')
        else:
            line.append('.')
    lines.append(line)

for line in lines:
    print(''.join(line))