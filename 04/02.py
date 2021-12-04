

class BingoBricka:
    def __init__(self, val):
        self.val = int(val)
        self.selected = False

    def set_selected(self, selected=True):
        self.selected = selected

class BingoBoard:
    def __init__(self, vals):
        self.vals = []
        self.rows = len(vals)
        self.cols = len(vals[0])
        for i in range(len(vals)):
            row = vals[i]
            for j in range(len(row)):
                if len(self.vals) <= i:
                    self.vals.append([BingoBricka(row[j])])
                else:
                    self.vals[i].append(BingoBricka(row[j]))

    def select(self, val):
        for i in range(self.rows):
            for j in range(self.cols):
                bricka = self.vals[i][j]
                if bricka.val == val:
                    bricka.set_selected()

    def get_bricka(self, row, col):
        return self.vals[row][col]

    def is_bingo(self):
        for i in range(self.rows):
            row = self.vals[i]
            col = [self.get_bricka(r, i) for r in range(self.cols)]
            if all([x.selected for x in row]) or all([x.selected for x in col]):
                return True
        return False

    def __str__(self):
        return str([[f"{x.val}, {x.selected}" for x in row] for row in self.vals])


brickor = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    nums = [int(val) for val in lines[0].strip().split(',')]

    for i in range(2, len(lines), 6):
        bricka = [lines[ii].split() for ii in range(i, i+5)]
        brickor.append(BingoBoard(bricka))

bingo_index = -1
winning_num = -1
winners = set()
for num in nums:
    for i in range(len(brickor)):
        if i in winners:
            continue
        bricka = brickor[i]
        bricka.select(num)
        if bricka.is_bingo():
            winners.add(i)
        if len(winners) == len(brickor):
            winning_num = num
            bingo_index = i
    if bingo_index != -1:
        break

print(bingo_index, 'has bingo')


winner = brickor[bingo_index]
sum = 0
for i in range(winner.rows):
    for j in range(winner.cols):
        bricka = winner.get_bricka(i, j)
        if not bricka.selected:
            sum += bricka.val

print(sum, winning_num, sum*winning_num)




# nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# b = BingoBoard(nums)

# b.select(1)
# b.select(5)
# b.select(9)
# b.select(12)

# print(b)
# print(b.is_bingo())
