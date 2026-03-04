import sys 

input=sys.stdin.readline
num=input()
a=list(map(int,input().split()))
# print(a)
# a.sort()
# print(a)
b=set(a)
b=sorted(b)
# print(b)
q=[]
w={}
for s,i in enumerate(b):
    w[i]=s
# for i in a:
#     q+=str(w[i])+' '
# print(q.strip())
for i in a:
    q.append(str(w[i]))
print(' '.join(q))