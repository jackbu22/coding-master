# import sys 
# input=sys.stdin.readline

# n,m=map(int,input().split())

# a=list(map(int,input().split()))

# p,q=map(int, input().split())
# z=sum(a[p-1:q])
# print(z)
# d=0
# for i in range(int(m)-1):
#     x,y=map(int, input().split())
#     if x==y:
#         print(a[x-1])
#     else:
#         if p<=x and q>y:                    #빼고 더하는게 다르다. 이거까지 해보자
#             d=z-sum(a[p-1:x])-sum(a[y-1:q])
#         elif p<=x and q<=y:
#             d=z-sum(a[p-1:x])+sum(a[q-1:y+1])
#         elif p>x and q>y:
#             d=z+sum(a[x-1:p])-sum(a[y-1:q])
#         elif p>=x and q<=y:
#             d=z+sum(a[x-1:p])+sum(a[q-1:y])
#         else:
#             d=sum(a[x-1:y])
#         print(d)
#         p=x 
#         q=y
#         z=d

#######시간초과가 나고 규칙이 다 더해서 전까지 더한거 빼며 되는거여서 dp문제인것이다

import sys 
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
d=[0]*(n+1)
d[1]=a[0]
answer=0

for i in range(2,n+1):
    d[i]=d[i-1]+a[i-1]
# print(d)

def dp(x,y):
    # 문제가 지금 1로 시작할때랑 xy숫자 같은떄니깐 나눠야함
    if x==y:
        print(a[x-1])
    else:
        answer=d[y]-d[x-1]
        print(answer)

for i in range(m):
    x,y=map(int,input().split())
    dp(x,y)

