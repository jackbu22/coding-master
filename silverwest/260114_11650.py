import sys
input = sys.stdin.readline

n = int(input())

dots = []
for i in range(n):
    dot = list(map(int,input().split()))
    dots.append(dot)

dots.sort(key=lambda x: (x[0], x[1]))

for dot in dots:
    print(dot[0], dot[1])