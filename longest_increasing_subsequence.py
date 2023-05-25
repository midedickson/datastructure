import time


# recursive dfs solution brute force
def slow_lis(arr):
    longest = 0

    def dfs(prevValue, index, sequence_count):
        if index >= len(arr):
            return sequence_count
        if arr[index] > prevValue:
            sequence_count += 1
            return max(
                dfs(arr[index], index + 1, sequence_count),
                dfs(arr[index], index + 2, sequence_count),
            )
        else:
            return max(
                dfs(prevValue, index + 1, sequence_count),
                dfs(prevValue, index + 2, sequence_count),
            )

    for i, _ in enumerate(arr):
        longest = max(longest, dfs(float("-inf"), i, 0))

    return longest


# fails because it is slow
tic = time.perf_counter()
print(slow_lis([10, 9, 2, 5, 3, 7, 101, 18]))
toc = time.perf_counter()

# display time taken to complete
print(f"Build finished in {toc - tic:0.4f} seconds")


def fast_lis(arr):
    """
    With DP
    """
    LIS = [1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)


# fails because it is slow
tic = time.perf_counter()
print(fast_lis([10, 9, 2, 5, 3, 7, 101, 18]))
toc = time.perf_counter()

# display time taken to complete
print(f"Build finished in {toc - tic:0.4f} seconds")
