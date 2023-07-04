import time


def fibonacci(n):
    """
    Recursive solution to fibonacci
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Running recursively...")
tic = time.perf_counter()
print(fibonacci(40))
toc = time.perf_counter()
# display time taken to complete
print(f"Build finished in {toc - tic:0.4f} seconds")


lookup = {}


def memo_dp_fib(n):
    """
    Dynammic Programming approach to Fibonacci using memoization
    """

    # Memory lookup with memoization
    if n not in lookup:
        if n <= 1:
            lookup[n] = n
        else:
            lookup[n] = memo_dp_fib(n - 1) + memo_dp_fib(n - 2)
    return lookup[n]


# print("Running with dp using memo...")
# tic = time.perf_counter()
# print(memo_dp_fib(40))
# toc = time.perf_counter()
# # display time taken to complete
# print(f"Build finished in {toc - tic:0.4f} seconds")


def tabulation_db_fib(n):
    lookup = {}
    lookup[0] = 0
    lookup[1] = 1
    i = 2
    while i <= n:
        lookup[i] = lookup[i - 1] + lookup[i - 2]
        i += 1
    return lookup[n]


print("Running with dp using tabulation")
tic = time.perf_counter()
print(tabulation_db_fib(40))
toc = time.perf_counter()
# display time taken to complete
print(f"Build finished in {toc - tic:0.4f} seconds")
