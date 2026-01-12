import sys

input= sys.stdin.readline

a,b=map(int,input().split())
# print('{}그리고{}'.format(a,b))

a_1=[]
b_1=[]
c=[]

a_2=[]
b_2=[]
d=[]


for i in range(1,a +1):
    if a%i==0:
        a_1.append(i)

for i in range(1,b +1):
    if b%i==0:
        b_1.append(i)

for i in a_1:
    for j in b_1:
        if i ==j:
            c.append(i)
최대공약수=c[-1]

for i in range(1,b+1):
    a_2.append(a*i)

for i in range(1,a+1):
    b_2.append(b*i)

for i in a_2:
    for j in b_2:
        if i ==j:
            d.append(i)
최소공배수=d[0]

print('{}\n{}'.format(최대공약수,최소공배수))