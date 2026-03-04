import sys
from collections import deque
def solve():

    input = sys.stdin.readline
    N,M = list(map(int, input().split())) # 행과 열의 개수
    whole = []

    # 행렬의 형태를 변경
    for i in range(N):
        a = list(map(int, input().split()))
        whole.append(a)
    
    # 1 = True, 0 = False로 변경
    for i in range(N):
        for j in range(M):
            if whole[i][j]==0:
                whole[i][j] = False
            elif whole[i][j] == 1 :
                whole[i][j] = True
            else:
                start_i = i
                start_j = j
    whole[start_i][start_j] = 0
    q = deque()
    q.append([start_i,start_j])

    while True:
        x = q.popleft()         
        i = x[0]
        j = x[1]
        z = whole[i][j]

        def news(a,b,z):        #a좌우, b상하, z현재거리
            if i+a < 0:
                return
            if j+b < 0:
                return
            if i+a >=N:
                return
            if j+b >=M:
                return

            move = whole[i+a][j+b] 
            if move is not False:
                if move is True:
                    whole[i+a][j+b] = z+1
                    q.append([i+a,j+b])

        news(-1,0,z)
        news(1,0,z)
        news(0,-1,z)
        news(0,1,z)
            
        if len(q) ==0:
            break
    
    for i in range(N):
        for j in range(M):
            if whole[i][j] is True:
                whole[i][j] = -1
            if whole[i][j] is False:
                whole[i][j] = 0

    for i in range(N):
        for j in range(M):
            print(whole[i][j], end=' ')
        print()




if __name__ == "__main__":                              
    solve()