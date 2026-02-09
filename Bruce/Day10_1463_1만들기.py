import sys


def solve():
    N = int(input())
    
    count = [0] * (N)

    for i in range(1,N):
        count[i]=count[i-1]+1
        if (i+1)%2==0:
            count[i]=min(count[i],count[i//2]+1)
        if (i+1)%3==0:
            count[i]=min(count[i],count[i//3]+1)

    
    print(count[N-1])

        


if __name__ == "__main__":
    solve()    