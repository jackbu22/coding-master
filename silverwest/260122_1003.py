import sys
input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())

#     cnt_0 = 0
#     cnt_1 = 0

#     stack = [n]  

#     while stack:
#         cur = stack.pop()

#         if cur == 0:
#             cnt_0 += 1
#         elif cur == 1:
#             cnt_1 += 1
#         else:
#             stack.append(cur - 1)
#             stack.append(cur - 2)

#     print(cnt_0, cnt_1)



dp_0 = [0] * 41
dp_1 = [0] * 41


dp_0[0], dp_1[0] = 1, 0 
dp_0[1], dp_1[1] = 0, 1  


for i in range(2, 41):
    dp_0[i] = dp_0[i-1] + dp_0[i-2]
    dp_1[i] = dp_1[i-1] + dp_1[i-2]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp_0[n], dp_1[n])