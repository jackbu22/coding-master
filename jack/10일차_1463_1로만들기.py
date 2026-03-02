# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째  줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 예제 입력 1 
# 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 10
# 예제 출력 2 
# 3
# 힌트
# 10의 경우에 10 → 9 → 3 → 1 로 3번 만에 만들 수 있다.


# import sys 
# input=sys.stdin.readline

# d=[0]*10*10*10*10*10*10
# d.append(0)
# d[1]=0
# d[2]=1
# d[3]=1

# for i in range(4,10*10*10*10*10*10+1):

#     count=0
#     a=i
#     t=d[i-1]+1
#     while i!=1:
#         if i%2==0:
#             i=i/2
#             count+=1
#         elif i%3==0:
#             i=i/3
#             count+=1
#         else:
#             i=i-1
#             count+=1
#     if count>=t:
#         d[a]=t
#     elif count<t:
#         d[a]=count
#     # print(num)


# num=input()
# num=int(num)

# print(d[num])





import sys 
input=sys.stdin.readline

num=input()
num=int(num)
d=[0]*(num+1)
if num>=1:
    d[1]=0  
if num>=2:
    d[2]=1
if num>=3:
    d[3]=1

if num>=4:
    for i in range(4,num+1):

        a=i
        t=d[i-1]+1
        # while i!=1:
        #     if i%2==0:
        #         i=i/2
        #         count+=1
        #     elif i%3==0:
        #         i=i/3
        #         count+=1
        #     else:
        #         i=i-1
        #         count+=1
        # # if count>=t:
        #     d[a]=t
        # elif count<t:
        #     d[a]=count
        
        if i%3==0 and i%2!=0:
            count=d[int(a/3)]+1
            d[a]=min(t,count)
        elif i%2==0 and i%3!=0:
            count=d[int(a/2)]+1
            d[a]=min(t,count)
        elif  i%3==0 and i%2==0:
            count2=d[int(a/2)]+1
            count3=d[int(a/3)]+1
            d[a]=min(t,count3,count2)
        elif  i%3!=0 and i%2!=0:
            d[a]=t
        
    # print(num)



print(d[num])
