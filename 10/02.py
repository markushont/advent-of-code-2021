with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

pairs = {
    '(': ')',
    '{': '}',
    '<': '>',
    '[': ']'
}

b_chunk = ['(', '{', '<', '[']
e_chunk = [')', '}', '>', ']']

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

incomplete_lines = []
for line in lines:
    openings = []
    for char in line:
        if char in b_chunk:
            openings.append(char)
        elif char == pairs[openings[-1]]:
            openings.pop()
        elif char in e_chunk and pairs[openings[-1]] != char:
            openings = []
            break
    if openings:
        incomplete_lines.append(openings)

tot_scores = []
for line in incomplete_lines:
    closing_chars = []
    for char in reversed(line):
        closing_chars.append(pairs[char])
    
    line_score = 0
    for char in closing_chars:
        line_score *= 5
        line_score += scores[char]
    tot_scores.append(line_score)

tot_scores = sorted(tot_scores)
print(tot_scores)
print(tot_scores[int(len(tot_scores)/2)])