import sys
input = sys.stdin.readline

res_list = {1 : 1, 2 : 2, 3 : 4}
for i in range(4, 11):
    res_list[i]= res_list[i-1] + res_list[i-2] + res_list[i-3]

t = int(input())

for i in range(t):
    n = int(input())
    print(res_list[n])


