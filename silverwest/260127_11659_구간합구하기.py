import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

sum_list = [0]             # 1번째부터 구하는 경우 
sum = 0

for i in range(len(nums)): # 구간 합 전부 구해놓고
    sum += nums[i]
    sum_list.append(sum)

 
for i in range(m):         #sum_list[j] - sum_list[i - 1]
    a, b = map(int, input().split())
    print(sum_list[b] - sum_list[a - 1])

