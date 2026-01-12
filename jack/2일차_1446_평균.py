import sys 
input=sys.stdin.readline

test=int(input().strip())
scores= list(map(float,input().split()))

scores.sort()

m=scores[-1]
new_scores=[]
add=0

for i in scores:
    q=float(i)/float(m)*100
    new_scores.append(q)

for i in new_scores:
    add+= float(i)

new_average=add/test

print(new_average)


