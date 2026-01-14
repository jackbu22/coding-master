import sys

n = int(input())

dots = []
for i in range(n):
    dot = list(map(int,input().split()))
    dots.append(dot)

dots.sort(key=lambda x: (x[0], x[1]))

print(dots)