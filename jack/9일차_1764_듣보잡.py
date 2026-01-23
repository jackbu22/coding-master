
#합집합(|), 교집합(&), 차집합(-) 구현하는 함수가 기억이 안나서 찾아봄
# https://wikidocs.net/1015

import sys 
input=sys.stdin.readline

N,M =map(int,input().split())

n=set({})
m=set({})
for i in range(N):
    n.add(input().strip())

for i in range(M):
    m.add(input().strip())
# print(n)
# print(m)
a=n&m
a=list(a)
a.sort()
print(len(a))
for i in a:
    print(i)