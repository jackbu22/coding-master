import sys 

input=sys.stdin.readline

numbers,lines=map(int,input().split())

q=set([])
w=[]
count=0
if lines==0:
    print(numbers)
elif lines!=0:
    c,d=input().split()
    q.add(c)
    q.add(d)
    for i in range(lines-1):
        a,b=input().split()
        if (a in q) or (b in q):
            q.add(a)
            q.add(b)
        elif (a not in q) and (b not in q):
            w.append((a,b))
    # print(w)

    changed = True
    while changed:
        changed = False
        w1 = []
        for (a, b) in w:
            if (a in q) or (b in q):
                if (a not in q) or (b not in q):
                    changed = True
                q.add(a)
                q.add(b)
            else:
                w1.append((a, b))
        w = w1
    count+=1
    # print(q)


    while w!=[]:
        e,f=w.pop()
        q.add(e)
        q.add(f)
        changed = True
        while changed:
            changed = False
            w1 = []
            for (a, b) in w:
                if (a in q) or (b in q):
                    if (a not in q) or (b not in q):
                        changed = True
                    q.add(a)
                    q.add(b)
                else:
                    w1.append((a, b))
            w = w1
        count+=1
    # print(q)
    # print(w)
    print(count+numbers-len(q))