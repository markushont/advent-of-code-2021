with open('input.txt', 'r') as f:
    cdata = [[int(x) for x in line.strip()] for line in f.readlines()]

class Point:
    def __init__(self, height, basin_coord = None, is_low=False):
        self.height = height
        self.is_low = is_low
        self.basin_coord = basin_coord

class Cave:
    def __init__(self, points):
        self.points = {r:{c: Point(points[r][c]) for c in range(len(points[r]))} for r in range(len(points)) }

        last_in_col = self.n_cols() - 1
        for r in range(last_in_col+1):
            row = self.points[r]
            last_in_row = self.n_rows() - 1
            for c in range(last_in_row+1):
                p = row[c].height
                if r != 0 and self.points[r-1][c].height <= p:
                    continue
                elif r != last_in_col and self.points[r+1][c].height <= p:
                    continue
                elif c != 0 and self.points[r][c-1].height <= p:
                    continue
                elif c != last_in_row and self.points[r][c+1].height <= p:
                    continue
                else:
                    self.points[r][c].is_low = True
                    self.points[r][c].basin_coord = (r, c)

    def n_cols(self):
        return len(self.points[0])

    def n_rows(self):
        return len(self.points)

def find_basin_coord(cave, r, c):
    if cave.points[r][c].height == 0:
        return None
    elif cave.points[r][c].basin_coord or cave.points[r][c].is_low:
        return cave.points[r][c].basin_coord

    if r != 0:
        coords = find_basin_coord(cave, r-1, c)
        if coords:
            return coords
    if r != len(cave.points) -1:
        coords = find_basin_coord(cave, r+1, c)
        if coords:
            return coords
    if c != 0:
        coords = find_basin_coord(cave, r, c-1)
        if coords:
            return coords
    if c != len(cave.points[r]) - 1:
        coords = find_basin_coord(cave, r, c+1)
        if coords:
            return coords

    return None

cave = Cave(cdata)

basin_coords = []
for r in range(cave.n_rows()):
    for c in range(cave.n_cols()):
        basin_coord = find_basin_coord(cave, r, c)
        if basin_coord not in basin_coords:
            basin_coords.append(basin_coord)

print(basin_coords)