with open('input.txt', 'r') as f:
    positions = sorted([int(x) for x in f.readlines()[0].strip().split(',')])
n_positions = len(positions)

def fibonacci(n):
    sum = 0
    current = n
    while current != 0:
        sum += current
        current -= 1
    return sum

    # if n == 0:
    #     return 0
    # else:
    #     return n + fibonacci(n-1)

fibs = {k:fibonacci(k) for k in range(max(positions)+1)}

def compute_cost(final_pos, positions):
    return sum(
        [fibs[abs(x-final_pos)] for x in positions]
    )

costs = [compute_cost(x, positions) for x in range(max(positions))]
print(min(costs))