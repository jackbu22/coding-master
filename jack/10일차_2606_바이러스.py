import sys 
input=sys.stdin.readline

q=input()
w=input().strip()

q_1=dict()
for s,i in enumerate(range(1,int(q)+1),start=1):
    q_1.update({s:i})

w=int(w)
# print(q_1)
m=[]
for i in range(int(w)):
    a=list(map(int,input().split()))
    a.sort()
    m.append(a)

m.sort()

if w==0:
    print(0)
else:
    a=m[0][0]
    b=m[0][1]
    del q_1[a]
    del q_1[b]
    # print(q_1)

    p=0 #쓰레기값
    k=1
    while k==1:
        k=0# 이걸 왜 쳐하시냐면 이걸해야 지워졌을때 다시 보게 해서 지우려고. 순서대로 지우면 안쳐지워지는것도 있으니깐
        for i in range(1,int(w)):
            e=m[i][0]
            r=m[i][1]
            
            # print(e)
            # print(w)
            if (e not in q_1) or (r not in q_1) or ((e not in q_1) and(r not in q_1)):
                try:
                    del q_1[e]
                    k=1
                except KeyError:
                    p=0
                try:
                    del q_1[r]
                    k=1
                except KeyError:
                    p=0

                # print(q_1)

    if 1 not in q_1:
        print(int(q)-len(q_1)-1)
    else:
        print(0)