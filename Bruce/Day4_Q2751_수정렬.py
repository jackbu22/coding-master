import sys

def solve():

    input = sys.stdin.readline
    N = int(input())

    Numbers =[]
    for i in range(N):
        Number = int(input())
        Numbers.append(Number)
    
    Numbers = list(set(Numbers))                   
    Numbers.sort()

    for i in range(len(Numbers)):
        print(Numbers[i])
    
        


if __name__ == "__main__":                              
    solve()