import random

# Randomly generated
def W(x, k, y):
    random.seed(k + 10*y)
    return random.randint(1, 10)  # Replace with actual weight function

def compute_topdown(n, W):

    memo = [[-1] * n for _ in range(n)]

    def TRI(x, y):
        raise NotImplementedError

    return TRI(0, n - 1)

def compute_bottomup(n, w):
    TRI = [[ -1 ] * n for _ in range(n)]  # Initialize the DP table
    for x in range(n - 1):  # Base case, notice the 0-based indexing
        TRI[x][x + 1] = 0

    # Fill the table anti-diagonally
    for delta in range(2, n):  # Delta is the gap between x and y
        for x in range(n - delta):  # Iterate over all valid x
            y = x + delta 
            t = float('inf')
            for k in range(x + 1, y):  # min over all x < k < y
                t = min(t, TRI[x][k] + w(x, k, y) + TRI[k][y])
            TRI[x][y] = t

    return TRI[0][n - 1]

n = 6
min_cost_td = compute_topdown(n, W)
min_cost_bu = compute_bottomup(n, W)

if min_cost_td == min_cost_bu:
    print(f"Top-down == Bottom-up: {min_cost_td}")
else:
    # Not the same
    assert(False)