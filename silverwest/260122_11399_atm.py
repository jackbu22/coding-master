import sys
input = sys.stdin.readline

n = int(input())

people = list(range(1, n + 1))

time = list(map(int,input().strip().split()))

inform = {}

for i in range(n):
    inform[people[i]] = time[i]

inform = sorted(inform.items(), key=lambda x: x[1])

result = 0
sum = 0

for key in inform:
    result += key[1]
    sum += result
print(sum)