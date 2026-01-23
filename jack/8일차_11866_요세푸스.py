# 문제
# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 예제 입력 1 
# 7 3
# 예제 출력 1 
# <3, 6, 2, 7, 5, 1, 4>
# Deque(데크)는 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조로, 주요 함수들은 양쪽 끝에 추가/삭제(append, appendleft, pop, popleft), 데이터 접근/확인(front/back, len, empty) 등이 있으며, 파이썬의 collections.deque와 C++ STL의 deque에서 다양한 메서드를 제공합니다. 
# 파이썬 collections.deque 주요 함수
# 추가(Append)
# append(x): 오른쪽 끝에 x 추가 (O(1))
# appendleft(x): 왼쪽 끝에 x 추가 (O(1))
# 삭제(Pop)
# pop(): 오른쪽 끝 원소 삭제 및 반환 (O(1))
# popleft(): 왼쪽 끝 원소 삭제 및 반환 (O(1))
# 기타 유용한 함수
# extend(iterable) / extendleft(iterable): 오른쪽/왼쪽 끝에 여러 원소 추가
# rotate(n): 원소를 n만큼 오른쪽으로 회전 (양수: 오른쪽, 음수: 왼쪽)
# clear(): 모든 원소 제거
# count(x): 원소 x의 개수 반환
# remove(x): 가장 왼쪽의 x 제거
# reverse(): 순서 뒤집기
# maxlen: 최대 길이 설정 (꽉 차면 반대편 원소 자동 삭제) 


import sys
from collections import deque
input=sys.stdin.readline
a,b= input().split()
# print(a,b)
a=int(a)
b=int(b)
c=deque([])
d=[]
e=[]
answer=''
for i in range(1,a+1):
    c.append(i)
# print(c)

while len(c)!=0:
    c.rotate(-b+1)
    # print(c)
    d.append(str(c.popleft()))

print('<'+', '.join(d)+'>')
