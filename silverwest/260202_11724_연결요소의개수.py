import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g_dict = {}

for _ in range(m):
    a, b= map(int, input().split())
    x = [a, b]
    if a not in g_dict:
        g_dict[a]=[]
    if b not in g_dict:
        g_dict[b]=[]
    g_dict[a].append(b)
    g_dict[b].append(a)

cnt = 0
visited = set()                             # 방문처리 할 집합

for start in g_dict:                         # 각 키에 대하여
    if start in visited:                    
        continue

    cnt += 1                                # 방문 안한 노드라면 (새로운 연결 요소의 시작)
    stack = [start]

    while stack:                            # 시작노드부터 DFS 시작
        cur = stack.pop()
        if cur in visited:          
            continue
        visited.add(cur)
        for v in g_dict[cur]:
            if v not in visited:
                stack.append(v)
        
print(cnt)