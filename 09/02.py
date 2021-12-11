with open('input.txt', 'r') as f:
    cdata = [[int(x) for x in line.strip()] for line in f.readlines()]

class Point:
    def __init__(self, coord, height, basin_coord = None, is_low=False):
        self.coord = coord
        self.height = height
        self.is_low = is_low
        self.basin_coord = basin_coord

class Cave:
    def __init__(self, points):
        self.points = {r:{c: Point((r, c), points[r][c]) for c in range(len(points[r]))} for r in range(len(points)) }
        self.n_rows = len(self.points.keys())
        self.n_cols = len(self.points[0].keys())

        last_in_col = self.n_cols - 1
        for r in range(last_in_col+1):
            row = self.points[r]
            last_in_row = self.n_rows - 1
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

    def get_right(self, r, c):
        return None if c >= self.n_cols-1 else self.points[r][c+1]
    
    def get_left(self, r, c):
        return None if c == 0 else self.points[r][c-1]

    def get_up(self, r, c):
        return None if r == 0 else self.points[r-1][c]

    def get_down(self, r, c):
        return None if r >= self.n_rows-1 else self.points[r+1][c]

    def get_low_points(self):
        ret = []
        for r in range(len(self.points)):
            for c in range(len(self.points[r])):
                if self.points[r][c].is_low:
                    ret.append(self.points[r][c])
        return ret

    def get_surrounding_points(self, r, c):
        return {
            self.get_right(r, c),
            self.get_up(r, c),
            self.get_left(r, c),
            self.get_down(r, c)
        }

    def get_points_in_basin(self, basin_r, basin_c):
        ret = set()
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if self.points[r][c].basin_coord == (basin_r, basin_c):
                    ret.add(self.points[r][c])
        return ret

cave = Cave(cdata)

basins = []
for b in cave.get_low_points():
    to_check = {b: cave.get_surrounding_points(b.coord[0], b.coord[1])}

    check_next = to_check
    while check_next:
        check_next = {}
        for base, points in to_check.items():
            for p in points:
                if not p:
                    continue
                if p.height > base.height and p.height < 9:
                    p.basin_coord = base.basin_coord
                    check_next.update({p: {x for x in cave.get_surrounding_points(p.coord[0], p.coord[1]) if x and not x.basin_coord}})
        to_check = check_next


    basins.append(cave.get_points_in_basin(b.coord[0], b.coord[1]))

basins_sorted = sorted([len(basin) for basin in basins], reverse=True)
print(basins_sorted[0]*basins_sorted[1]*basins_sorted[2])