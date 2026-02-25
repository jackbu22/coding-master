import sys
from collections import deque
def solve():

    input = sys.stdin.readline
    N,M = list(map(int, input().split())) # 행과 열의 개수
    whole = []

    # 행렬의 형태를 변경
    for i in range(M):
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
            if j+b >=N:
                return

            move = whole[i+a][j+b] 
            if move != False:
                if move == True:
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
            print(whole[i][j], end=' ')
            # if j == M-1:
            #     print('\n')



    # # 계산의 편의를 위에 상하좌우에 False 추가
    # for i in range(N):
    #     whole[i].append(False)
    #     whole[i].insert(0,False)

    # b = []    
    # for i in range(M+2):
    #     b.append(False)
    # whole.append(b)
    # whole.insert(0,b)


    # for k in range(3,N+M+2):
    #     for i in range(1,N+1):
    #         for j in range(1,M+1):
    #             if i+j==k:
    #                 if whole[i][j]==1:
    #                     something = []
    #                     w = whole[i-1][j]
    #                     e = whole[i+1][j] 
    #                     s = whole[i][j-1]
    #                     n = whole[i][j+1]
    #                     something.append(w)
    #                     something.append(e)
    #                     something.append(s)
    #                     something.append(n)
    #                     if any(x > 1 for x in something):
    #                         whole[i][j] = min(x for x in something if x > 1)+1

    # del whole[-1]
    # del whole[0]
    # for i in range(N):
    #     del whole[i][-1]
    #     del whole[i][0]
                    
    # print(whole)

if __name__ == "__main__":                              
    solve()