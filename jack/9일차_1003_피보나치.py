# import sys
# from bisect import bisect_left,bisect_right
# input=sys.stdin.readline

# zero=[]
# one=[]
# def fibonacci(y,x):
#     if x == 0:
#         # print("0")
#         return [0]
#     elif x == 1 :
#         # print("1")
#         return [1]
#     else :
#         return fibonacci(y,x-1) + fibonacci(y,x-2)
    
# num=input()

# for i in range(int(num)):
#     q=input()
#     one=fibonacci(zero,int(q))


#     one.sort()
#     a=bisect_right(one,0)
#     b=bisect_left(one,0)
#     q=a-b
#     c=bisect_right(one,1)
#     d=bisect_left(one,1)
#     w=c-d

#     print(str(q)+' '+str(w))


zero=[1,0]
one=[0,1]

for i in range(1,42):
    # if i ==1:
    #     print(str(zero[i-1])+' '+str(one[i-1]))
    # elif i==2:
    #     print(str(zero[i-1])+' '+str(one[i-1]))
    if i!=1 and i!=2:
        z=zero[i-3]+zero[i-2]
        o=one[i-3]+one[i-2]
        zero.append(z)
        one.append(o)

# print(zero)
# print(one)

num=input()
for i in range(int(num)):
    n=input().strip()
    print(str(zero[int(n)])+' '+str(one[int(n)]))