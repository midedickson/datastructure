[
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
]


def max_wrapped_presents(k, a, d, m, b, C):
    dp = [[[-float('inf')] * (1 << m) for _ in range(m+1)] for _ in range(k+1)]
    dp[0][0][0] = 0

    for mask in range(1, 1 << m):
        dp[0][0][mask] = -float('inf')

    for i in range(1, k+1):
        for j in range(1, m+1):
            for mask in range(1 << m):
                dp[i][j][mask] = dp[i-1][j][mask]

                for p in range(m):
                    if ((mask >> p) & 1) and C[i-1][p]:
                        dp[i][j][mask] = max(dp[i][j][mask], dp[i-1][j][mask ^ (1 << p)] + min(a[i-1], b[p]))

    for j in range(1, m+1):
        for mask in range(1 << m):
            dp[k][j][mask] = max(dp[k][j][mask], dp[k][j-1][mask])

    max_wrapped = 0
    for mask in range(1 << m):
        max_wrapped = max(max_wrapped, dp[k][m][mask])

    return max_wrapped


def max_children_presents(n, m, D, children, shopping_centers):
    # Create a bipartite graph
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            distance = calculate_distance(children[i], shopping_centers[j])
            if distance <= D:
                graph[i].append(j)

    # Initialize an empty matching
    matching = [-1] * m

    # Run matching algorithm
    for child in range(n):
        visited = [False] * n
        if dfs(child, graph, visited, matching):
            matching[child] = -1

    # Count the number of children in the matching
    max_children = matching.count(-1)
    return max_children


def dfs(child, graph, visited, matching):
    for shopping_center in graph[child]:
        if not visited[shopping_center]:
            visited[shopping_center] = True
            if matching[shopping_center] == -1 or dfs(matching[shopping_center], graph, visited, matching):
                matching[shopping_center] = child
                return True
    return False


def calculate_distance(point1, point2):
    # Implement the distance calculation between two points (e.g., Euclidean distance)
    pass


def min_distance(n, m, children, shopping_centers):
    low = 0
    high = float('inf')

    while low <= high:
        mid = (low + high) // 2
        max_children = max_children_presents(n, m, mid, children, shopping_centers)

        if max_children == n:
            high = mid - 1
        else:
            low = mid + 1

    if low > high:
        return -1

    return low
