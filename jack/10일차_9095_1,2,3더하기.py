# # 1, 2, 3 더하기 다국어
# # 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# # 1 초 (추가 시간 없음)	512 MB	153466	102117	71350	65.150%
# # 문제
# # 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# # 1+1+1+1
# # 1+1+2
# # 1+2+1
# # 2+1+1
# # 2+2
# # 1+3
# # 3+1
# #  정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
 
# # 입력
# # 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

# # 출력
# # 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

# # 예제 입력 1 
# # 3
# # 4
# # 7
# # 10
# # 예제 출력 1 
# # 7
# # 44
# # 274

import sys 
input=sys.stdin.readline
number=input().strip()
number=int(number)
d=[0]*(12)
e=[[3],[1,2],[1,1,1]]
f=[[2],[1,1]]
g=[[1]]

z=[1]*12
for i in range(1, 12):
    z[i]=z[i-1]*i

# print(z)



for i in range(1,12):
    # c=[[[0]],[[0]],[[0]],[[0]]]
    # h=[[[0]]]
    # p=[[[0]]]

    t=0
    a=i//3
    b=i%3
    for q in range(a+1): # 3의 갯수 경우의수
        r = i - 3*q
        for w in range(r//2 + 1): #2,1의 갯수 경우의수
            s = r - 2*w
            k = s + w + q
            t += z[k] // (z[s] * z[w] * z[q])

    d[i]=t

for qw in range(number):
    we=input().strip()
    we=int(we)
    print(d[we])










#     # for j in range(int(a)):
#     #     c[j]=e
#     # if b==0:
#     #     pass
#     # elif b==1:
#     #     h[0]=g
#     # elif b==2:
#     #     p[0]=f
#     # # print(c)
#     # print(c)
#     # print(p)
#     # print(h)
#     # for k in c[0]:
#     #     for l in p[0]:
#     #         for m in h[0]:
#     #             s=k+l+m
#     #             s.sort()
#     #             z.append(s)
#     # z=set(z)

#     # print(z)



    