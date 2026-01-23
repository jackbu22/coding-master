import sys


def solve():
    N = int(input())
    
    count = [0]

    for i in range(N-1):
        count.append(1000)

    for i in range(1,N):
        if (i+1)%2==0:
            count[i]=min(count[i-1]+1,count[(i+1)//2-1]+1)
        if (i+1)%3==0:
            count[i]=min(count[i-1]+1,count[(i+1)//3-1]+1)
        count[i]=min(count[i-1]+1,count[i])

    
    print(count[N-1])

        


if __name__ == "__main__":
    solve()    
