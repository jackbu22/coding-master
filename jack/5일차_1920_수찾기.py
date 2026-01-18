import sys


input= sys.stdin.readline

Nnumber=int(input())
Nnumbers=set(map(int,input().split()))

Mnumber=int(input())
Mnumbers=list(map(int,input().split()))

answer=[]

for i in Mnumbers:
    if i in Nnumbers:
        answer.append(1)
    else:
        answer.append(0)
for i in answer:
    print(i)
