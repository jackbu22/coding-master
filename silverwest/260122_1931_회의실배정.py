import sys
input = sys.stdin.readline

n = int(input())

informs = []

for i in range(n):
    inform = list(map(int,(input().strip().split())))
    informs.append(inform)

informs.sort(key = lambda x : (x[1], x[0]))


schedules = [informs[0]]


for i in range(1, n):
    if schedules[-1][1] <= informs[i][0]:
        schedules.append(informs[i])

print(len(schedules))







