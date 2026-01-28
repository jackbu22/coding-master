import sys
input = sys.stdin.readline

# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, farm, m, n):
    ## 상하좌우로 연결된 배추를 탐색, 방문한 배추는 0으로 바꿔서 다시 방문하지 않도록 처리

    stack = [(x, y)]
    farm[y][x] = 0  # 시작 지점 방문 처리

    while stack:
        cur_x, cur_y = stack.pop()
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]

            # 범위 안에 있고 배추라면
            if 0 <= next_x < m and 0 <= next_y < n and farm[next_y][next_x] == 1:
                farm[next_y][next_x] = 0      # 방문 처리
                stack.append((next_x, next_y))


t = int(input())  

for i in range(t):
    m, n, k = map(int, input().split()) 


    farm = [[0] * m for i in range(n)]


    for i in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    count = 0  

    # 전체 밭을 돌면서
    for y in range(n):
        for x in range(m):
            # 배추를 발견하면
            if farm[y][x] == 1:
                dfs(x, y, farm, m, n)  # 연결된 배추 확인
                count += 1             

    print(count)
