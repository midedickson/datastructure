arr = [2, 1, 3]


def min_cost_balance_pole(rods):
    n = len(rods)

    # Sort rods in non-decreasing order
    rods.sort()

    # Initialize a 2D table to store the minimum cost of welding rods
    dp = [[0] * n for _ in range(n)]

    # Fill in the table using dynamic programming
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            # Try all possible splits and find the minimum cost
            for k in range(i, j):
                cost = rods[i] + rods[j] + dp[i][k] + dp[k + 1][j]
                dp[i][j] = min(dp[i][j], cost)

    # Return the minimum cost to create the balance pole
    return dp[0][n - 1]


# Example usage
rods = [2, 1, 3]
min_cost = min_cost_balance_pole(rods)
print("Minimum cost to create the balance pole:", min_cost)


def merge(left, right):
    merged = []
    instability = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            instability += left[i] * (len(right) - j)
            i += 1
        else:
            merged.append(right[j])
            instability += right[j] * (len(left) - i)
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, instability


def min_instability(rods):
    n = len(rods)
    if n <= 1:
        return rods
    mid = n // 2
    left = min_instability(rods[:mid])
    right = min_instability(rods[mid:])
    return merge(left, right)[0]


# Example usage
rods = [2, 4, 6, 5, 2]
ordered_rods = min_instability(rods)
print("Order of rods with minimal instability:", ordered_rods)
