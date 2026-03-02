# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4
# 힌트
# 수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.
import sys
from collections import deque
input = sys.stdin.readline
a,b=map(int,input().split())
# # print(a,b)
# c=0
# count=0
# def qw(a,b):
#     if a==b:
#         return count
#     count+=1
#     return qw(2*a,b),qw(a-1,b),qw(a+1,b)

# print(count)
visited=[False]*100002
queue=deque([(a,0)])
c=0
d=0
while queue:
    c,d=queue.popleft()

    if c==b:
        print(d)
        break

    for i in (c-1,c+1,2*c):
        if 0<=i<=100002 and not visited[i]:
            visited[i]=True
            queue.append((i,d+1))