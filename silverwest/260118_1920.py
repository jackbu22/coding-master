import sys
input = sys.stdin.readline

n = int(input())
list_a = set(map(int, input().split()))

m = int(input())
list_b = list(map(int, input().split()))

for i in range(m):
    if list_b[i] in list_a:
        print(1)
    else:
        print(0)
