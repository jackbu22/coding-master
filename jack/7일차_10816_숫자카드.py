import sys
from bisect import bisect_left,bisect_right
input=sys.stdin.readline

N_number=int(input())
N=list(map(int,input().split()))
M_number=int(input())
M=list(map(int,input().split()))

N.sort()

# print(M)
# print(N)
answer=[]
for i in M:
    a=bisect_right(N,i)
    b=bisect_left(N,i)
    c=a-b
    answer.append(str(c))
print(" ".join(answer))

#https://programming119.tistory.com/196
#https://laurent.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EC%A4%84%EC%9D%B4%EA%B8%B0