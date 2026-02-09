import sys
from operator import itemgetter
from collections import Counter


component = []
for i in range(10):
    component.append([])

component[0] = [[1,1]]                          #2
component[1] = [[2,1],[1,1,1]]                  #3
component[2] = [[3,1],[2,2],[2,1,1],[1,1,1,1]]  #4


for i in range(3,10):
    copied = component[i-1][0].copy()
    if (i+2)%3==0:
        copied[-1] = 3
    elif (i+2)%3==1:
        copied.append(1)
    elif (i+2)%3==2:
        copied[-1] = 2
    component[i].append(copied)


for i in range(3,10):
    for j in range(1,len(component[i-1])+1):
        component[i].append([])
        new = component[i-1][j-1].copy()
        new.append(1)
        component[i][j] = new
    for k in range(1,len(component[i-1])+1):
        if k > 1:
            if component[i-1][k-1].count(1)==1:
                nnew = component[i-1][k-1].copy()
                nnew.remove(1)
                nnew.append(2)
                component[i].append(nnew)

    if component[i][0] == component[i][1]:
        del component[i][1]

# 지금까지 모든 컴포넨트들을 구했음

def factorial(n):
    x =1
    for i in range(n):
        x = x*(i+1)
    return x

def result(list):
    sum = 0
    for i in range(len(list)):
        count = Counter(list[i])
        result = factorial(len(list[i]))//factorial(count[1])//factorial(count[2])//factorial(count[3])
        sum+=result
    print(sum)
    return sum

def solve():

    input = sys.stdin.readline
    N = int(input())
    for i in range(N):
        M = int(input())
        if M ==1:
            print(1)
        elif M==2:
            print(2)
        elif M==3:
            print(4)
        else:
            result(component[M-2])

        

if __name__ == "__main__":                              
    solve()