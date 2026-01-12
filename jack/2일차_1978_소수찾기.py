import sys
input=sys.stdin.readline

size = int(input().strip())
number = list(map(int,input().split()))
answer=0

for i in range(size):
    약수=[]
    for q in range(1,number[i]+1):
        
        if int(number[i])%q==0:
            약수.append(q)

    if len(약수)==2:
        answer+=1
print(answer)
