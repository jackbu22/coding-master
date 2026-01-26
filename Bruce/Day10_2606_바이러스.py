import sys
from operator import itemgetter


def virus(a,b):

    length = len(a)
    for i in range(len(b)):


        if b[i][0] in a:
            if b[i][1] in a:
                continue
            a.append(b[i][1])

        if b[i][1] in a:
            if b[i][0] in a:
                continue
            a.append(b[i][0])
    
    if len(a)==length:
        return



    return virus(a,b)
        


def solve():

    input = sys.stdin.readline
    N = int(input())            
    M = int(input())  

    listss = []

    for i in range(M):
        a = list(map(int, input().split()))
        listss.append(a)

    result = [1]

    virus(result,listss)

    print(len(result)-1)

        



if __name__ == "__main__":                              
    solve()