
import sys

def solve():
    input = sys.stdin.readline
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    Numbers = list(map(int, input().split()))

    Max_value = 0
    Min_error = 1000000
    for i in range(N):
        for j in range(1,N):
            for k in range(2,N):
                if i== j or i==k or j==k:
                    continue
                else:
                    value = Numbers[i]+Numbers[j]+Numbers[k]
                    error = M - Numbers[i]-Numbers[j]-Numbers[k]
                    if value > M:
                        continue
                    else:
                        if error < Min_error:
                            Max_value = value
                            Min_error = error
    
    print(Max_value)
    





if __name__ == "__main__":                              
    solve()
