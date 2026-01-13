import sys
import math
def solve():
    Numbers = list(map(int, input().split()))
    a = Numbers[0]
    b = Numbers[1]
    
    x = 1
    y = 1
    for i in range(1,b+1):
        x *= a-i+1
        y *= i
    print(dir(list))

    print(x//y)

if __name__ == "__main__":                              
    solve()