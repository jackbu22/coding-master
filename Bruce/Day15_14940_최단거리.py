import sys


"""def func(list):

    for i in range(1,len(list)-1):
        """


def solve():

    input = sys.stdin.readline
    N,M = list(map(int, input().split())) # 행과 열의 개수
    whole = []

    # 행렬의 형태를 변경
    for i in range(M):
        a = list(map(int, input().split()))
        whole.append(a)

    # 계산의 편의를 위에 상하좌우에 0추가
    for i in range(N):
        whole[i].append(0)
        whole[i].insert(0,0)

    b = []    
    for i in range(M+2):
        b.append(0)
    whole.append(b)
    whole.insert(0,b)

    for k in range(3,N+M+2):
        for i in range(1,N+1):
            for j in range(1,M+1):
                if i+j==k:
                    if whole[i][j]==1:
                        something = []
                        w = whole[i-1][j]
                        e = whole[i+1][j] 
                        s = whole[i][j-1]
                        n = whole[i][j+1]
                        something.append(w)
                        something.append(e)
                        something.append(s)
                        something.append(n)
                        if any(x > 1 for x in something):
                            whole[i][j] = min(x for x in something if x > 1)+1

    del whole[-1]
    del whole[0]
    for i in range(N):
        del whole[i][-1]
        del whole[i][0]
                    
    print(whole)

if __name__ == "__main__":                              
    solve()