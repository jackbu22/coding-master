import sys

def solve():
    input = sys.stdin.readline
    N = int(input())   
    x = list(map(int, input().split())) 

    sorted_x = list(set(x))
    sorted_x=sorted(sorted_x)
    index = {}
    for i in range(len(sorted_x)):
        if sorted_x[i] not in index.keys():
            index[sorted_x[i]] = i


    for i in x:
        print(index[i], end=' ')

if __name__ == "__main__":                              
    solve()