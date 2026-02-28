def count_unreachable_pairs(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    component_sizes = []
    def dfs(node):
        stack = [node]
        size = 0
        visited[node] = True
        while stack:
            curr = stack.pop()
            size += 1
            for nei in graph[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        return size
    for i in range(n):
        if not visited[i]:
            component_sizes.append(dfs(i))
    total_pairs = 0
    remaining = n
    for size in component_sizes:
        remaining -= size
        total_pairs += size * remaining

    return total_pairs


if __name__ == "__main__":
    n = 5
    edges = [(0, 1), (2, 3)]
    print(count_unreachable_pairs(n, edges))