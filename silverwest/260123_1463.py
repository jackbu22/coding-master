import sys
input = sys.stdin.readline

n = int(input())

cnt_list = [0] * 1000001


for i in range(2, n + 1):
    cnt_list[i] = cnt_list[i - 1] + 1
    if i % 2 == 0:
        cnt_list[i] = min(cnt_list[i], cnt_list[i // 2] + 1)
    if i % 3 == 0:
        cnt_list[i] = min(cnt_list[i], cnt_list[i // 3] + 1)

print(cnt_list[n])
