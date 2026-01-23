import sys


def solve():
    T = int(input())
    x=[0,1]
    for i in range(40):
        x.append(x[i+1]+x[i])
    for i in range(T):
        N = int(input())
        if N ==0:
            print(1,0)
        else:
            print(x[N-1],x[N])


if __name__ == "__main__":
    solve()    
