import sys 
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

m, n = map(int,input().split())
tomatoes = [list(map(int, input().split())) for i in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j))            # 익은 토마토(시작점) 큐 만들기

while queue:
    cur_y, cur_x = queue.popleft()

    for d in range(4):
        next_x = cur_x + dx[d]
        next_y = cur_y + dy[d]

        # 범위 안에 있고 0이라면 옆에 꺼의 +1
        if 0 <= next_x < m and 0 <= next_y < n and tomatoes[next_y][next_x] == 0:
            tomatoes[next_y][next_x] = tomatoes[cur_y][cur_x] + 1      # 날짜 처리
            queue.append((next_y, next_x))
            


## 0이 있으면 -1, 모든 토마토가 익어있는 상태 즉 2번이라면 0 출력, 아니면 max에 -1
flag = True
answer = 0
for i in range(n):
    for j in range(m):
            if tomatoes[i][j] == 0:
                flag = False
            answer = max(answer, tomatoes[i][j])

if not flag:
    print(-1)
else:
    print(answer - 1)