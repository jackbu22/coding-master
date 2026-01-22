import sys

input= sys.stdin.readline

number=int(input())
q=[]
for i in range(number):
    a=str(input().split())
    q.append(a)
# print(q)

for i in q:
    q=[]
    w=[]
    # print(i)
    t= i[2:-2]
    for j  in t:
        q.append(j)
    # print(q)
    for i in q:
        w.append(i)
        if len(w)!=1:
            if w[-2]=='(' and w[-1]==')':
                w.remove(w[-2])
                w.remove(w[-1])
    # print(w)
    if len(w)>0:
        print('NO')
    else:
        print('YES')
    

