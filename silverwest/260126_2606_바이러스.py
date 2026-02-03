import sys
input = sys.stdin.readline

v = int(input())
v_list = list(range(1, v + 1))

e = int(input())
e_dict = {v: [] for v in v_list} #딕셔너리 초기화, v를 키로 빈 리스트를 값으로 저장

for i in range(e):
    a, b = map(int, input().split())
    e_dict[a].append(b) # 무방향 그래프이기에 쌍방 저장
    e_dict[b].append(a)

def dfs(graph, node):
    result = []
    visited = set()

    def dfs_visit(u):
        if u in visited:
            return
        
        visited.add(u)
        result.append(u)

        for v in graph[u]:
            dfs_visit(u)

    dfs_visit(node)
    return(result)


print(len(dfs(e_dict, 1)))