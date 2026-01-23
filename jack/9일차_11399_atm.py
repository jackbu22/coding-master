import sys
input=sys.stdin.readline

people=int(input())

time=list(map(int,input().split()))
time.sort()
# print(time)
sum=0
for i in range(1,people+1):
    a = time[:i]
    for j in a:
        sum+=int(j)
print(sum)