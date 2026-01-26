### DFS

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                stack.append(v)

    return visited



### BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        u = queue.popleft()
        if u in visited:
            continue

        visited.add(u)

        for v in graph[u]:
            if v not in visited:
                queue.append(v)

    return visited
