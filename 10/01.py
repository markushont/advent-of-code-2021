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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

corrupt_endings = []
for line in lines:
    chunks = []
    for char in line:
        if char in b_chunk:
            chunks.append(char)
        elif char == pairs[chunks[-1]]:
            chunks.pop()
        elif char != pairs[chunks[-1]]:
            corrupt_endings.append(char)
            break

score = sum([corrupt_endings.count(c) * scores[c] for c in set(corrupt_endings)])

print(score)
