import sys
input=sys.stdin.readline

q=[0]*1001
q[1]=1
q[2]=2
for i in range(3,1001):
    q[i]=q[i-1]+q[i-2]
number=input().strip()
number=int(number)
print(q[number]%10007)#  문제좀 읽자

 