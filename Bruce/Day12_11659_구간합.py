import sys

def solve():

    input = sys.stdin.readline
    N,M = list(map(int, input().split())) # 수의 개수
    Numbers = list(map(int, input().split())) # 수 종류
    
    accumulation = [0]
    a = 0
    for i in range(N):
        a+= Numbers[i]
        accumulation.append(a)
    for i in range(M):
        start, end = list(map(int, input().split()))
        print(accumulation[end]-accumulation[start-1])





if __name__ == "__main__":                              
    solve()