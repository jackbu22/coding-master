import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    
    Standard = [1,2,3]
    while Standard[-1] <= N:
        Standard.append(Standard[-1]*2-1)
    S =0
    for i in range(len(Standard)):
        if i == len(Standard) - 1:
            if N >= Standard[i]:
                S = Standard[i]
        else:
            if Standard[i] <= N < Standard[i+1]:
                S = Standard[i]
        
    if S == 1: 
        print(S)
    
    elif S==2:
        print(S)
    
    else:
        print(2+(N-S)*2)
    



if __name__ == "__main__":
    solve()
