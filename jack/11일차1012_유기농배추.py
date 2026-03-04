# q=[[1	,1	,0	,0	,0	,0	,0	,0	,0	,0    ,0],
#   [0	,1	,0	,0	,0	,0	,0	,0	,0	,0    ,0],
#   [0	,0	,0	,0	,1	,0	,0	,0	,0	,0    ,0],
#   [0	,0	,0	,0	,1	,0	,0	,0	,0	,0    ,0],
#   [0	,0	,1	,1	,0	,0	,0	,1	,1	,1    ,0],
#   [0	,0	,0	,0	,1	,0	,0	,1	,1	,1    ,0],
#   [0	,0	,0	,0	,0	,0	,0	,0	,0	,0    ,0]]



import sys
input= sys.stdin.readline
total=input().strip()
 
for p in range(int(total)):
    m,n,k=map(int,input().split())
    #  m=10   n=6   k=14

    m=int(m)
    n=int(n)
    k=int(k)
    q=[]
    # q=[[0]*(m+1)]*(n+1)
    for  c in range(n+1):
        q.append([0]*(m+1))
    # print(q)

    for i in range(k):
        x,y=map(int,input().split())
        q[y][x]=1
    # o = copy.deepcopy(q)
    # print(q)
    answer=0
    for i in range(n):
        for j in range(m):
            if q[i][j] ==1:
                # if q[i+1][j]==1 or q[i][j+1]==1 :
                #     q[i][j]=
                answer+=1
                one = [[i, j]]
                q[i][j] = 0

                while len(one)!=0:
                    z = one.pop()
                    y=z[0]
                    x=z[1]
                    # 위
                    if y-1 >= 0 and q[y-1][x] == 1:
                        q[y-1][x] = 0
                        one.append([y-1, x])

                    # 아래
                    if y+1 < n and q[y+1][x] == 1:
                        q[y+1][x] = 0
                        one.append([y+1, x])

                    # 왼
                    if x-1 >= 0 and q[y][x-1] == 1:
                        q[y][x-1] = 0
                        one.append([y, x-1])

                    # 오
                    if x+1 < m and q[y][x+1] == 1:
                        q[y][x+1] = 0
                        one.append([y, x+1])

    # print(q)
    print(answer)





# 같은행은 index가 1차이 나야 연결되고 위아래는 인덱스가 같아야함
# w=[]
# for i in range(10):
#     a=q[0][i]+q[1][i]
#     w.append(a)


# print(w)

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# import sys

# input= sys.stdin.readline
# total=input().strip()
# x,y,z=map(int,input().split())

# d=[[0]*x]*y
# print(d)