import sys
input = sys.stdin.readline

t = int(input())
m, n, k = map(int, input().split())


farm = [[0] * m for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    print(farm[y][x])
    farm[y][x] = 1
    print(farm)