import sys
from collections import Counter #개수 세는 라이브러리

input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))
counts = Counter(cards)

m = int(input())

nums = list(map(int, input().split()))

result = [counts[num] for num in nums] #리스트 내 요소들을 하나씩 꺼내서 counts 딕셔너리에서 값 가져오기

print(*(result)) #리스트를 언팩해서 출력