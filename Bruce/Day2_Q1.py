
import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    Numbers = list(map(int, input().split()))

    Total = []
    for i in Numbers:
        if i==2:
            Total.append(0)
        
        if i%2 ==1:
            div = []
            for j in range(1,i+1):
                if i%j ==0:
                    div.append(0)
            if len(div)==2:
                Total.append(0)
    print(len(Total))


if __name__ == "__main__":                              
    solve()


    

