import sys

input= sys.stdin.readline

N,M= map(int,input().split())
a=1
b=1
c=1
for i in range(1,N +1):
    a*=i

for i in range(1,M+1):
    b*=i

for i in range(1,(N-M)+1):
    c*=i
print(int(a/b/c))