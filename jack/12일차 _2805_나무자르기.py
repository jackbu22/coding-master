import sys 

input=sys.stdin.readline

trees,left=map(int,input().split())
a=list(map(int,input().split()))

# # a=[4, 42, 40, 26, 46]
# a.sort()
# print(a)

# left=20
high = max(a)
q=high-left
# high=a[-1]
number=0
# for i in reversed(range(q,a[-1]+1)): 
while q<=high:
    # w=[]
    w=0
    i=(q+high)//2
    for j in a:
        l=j-i
        # if j-i<=0:
        #     pass
        if l>=0:
            # w.append(j-i)
            w+=l
            if w >= left:   
                break
    if w>=left:
        number=i
        q=i+1
    else:
        high=i-1
    
        
print(number)

