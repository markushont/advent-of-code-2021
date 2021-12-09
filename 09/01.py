with open('input.txt', 'r') as f:
    cave = [[int(x) for x in line.strip()] for line in f.readlines()]

low_points = []
last_in_col = len(cave) - 1
for r in range(last_in_col+1):
    row = cave[r]
    last_in_row = len(row) - 1
    for c in range(last_in_row+1):
        p = row[c]
        if r != 0 and cave[r-1][c] <= p:
            continue
        elif r != last_in_col and cave[r+1][c] <= p:
            continue
        elif c != 0 and cave[r][c-1] <= p:
            continue
        elif c != last_in_row and cave[r][c+1] <= p:
            continue
        else:
            low_points.append(p)

print(sum([x+1 for x in low_points]))
