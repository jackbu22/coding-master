import sys

def fun(M,N,listss):
    count = 2

    for i in range(M):
        for j in range(N):
            if listss[i][j] ==1 :
                if i!=0 and listss[i-1][j] !=1 and listss[i-1][j] !=0:
                    listss[i][j] = listss[i-1][j]
                elif j!=0 and listss[i][j-1] !=1 and listss[i][j-1] !=0:
                    listss[i][j] = listss[i][j-1]
                else:
                    listss[i][j]=count
                    count+=1
    for i in range(M):
        for j in range(N):
            if listss[i][j]!=0:
                if i!= 0 and j!=0 and listss[i-1][j] !=0 and listss[i][j-1] !=0:
                    if listss[i-1][j] != listss[i][j-1]:
                        right = min(listss[i-1][j],listss[i][j-1])
                        wrong = max(listss[i-1][j],listss[i][j-1])
                        listss[i][j] = right
                        for k in range(M):
                            for z in range(N):
                                if listss[k][z] == wrong:
                                    listss[k][z] = right

                elif i!=0 and j==0 and listss[i-1][j] !=0:
                    if listss[i][j]!=listss[i-1][j]:
                        listss[i][j] = listss[i-1][j]
                             
    return listss

def solve():
    input = sys.stdin.readline

    T = int(input())
    for i in range(T):
        M, N, K = map(int, input().split())
        array = []
        for i in range(M):
            row = []
            for j in range(N):
                row.append(0)
            array.append(row)
        
        for _ in range(K):
            x,y = map(int, input().split())
            array[x][y] =1
        k = fun(M,N,array)
        for i in range(1,len(k)):
            k[0].extend(k[i])
        result1= set(k[0])
        if 0 in result1:
            result1.remove(0)
        print(len(result1))

if __name__ == "__main__":                              
    solve()