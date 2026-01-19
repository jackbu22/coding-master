import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))
counts = Counter(cards)

m = int(input())

nums = list(map(int, input().split()))

result = [counts[num] for num in nums]

print(*(result))