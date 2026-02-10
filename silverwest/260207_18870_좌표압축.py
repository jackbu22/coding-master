import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int, input().split()))

sorted_set = sorted(set(points))    #딕셔너리 만들기 위해서 고유값 정렬 집합 만들어주기

idx = {}

for i, v in enumerate(sorted_set):  #파이썬에서 인덱스랑 요소를 같이 반환하고 싶을때 enumerate함수
    idx[v] = i                      #고유한 인덱스 -> 좌표 압축

result =[]

for i in points:
    result.append(idx[i])

print(*result)