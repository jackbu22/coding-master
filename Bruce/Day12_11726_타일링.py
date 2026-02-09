import sys


def factorial(n):
    x =1
    for i in range(n):
        x = x*(i+1)
    return x
    
def combination(a,b):
    result = factorial(a)//factorial(a-b)//factorial(b)

    return result

def tile(N):
    sum=1
    for i in range(N//2):
        sum+=combination(N-i-1,i+1)

    return sum


def solve():

    input = sys.stdin.readline
    N = int(input())
    print(tile(N)%1007) 
    





if __name__ == "__main__":                              
    solve()