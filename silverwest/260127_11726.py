# 1이랑 2로 더하기 문제잖아!!
# DP 문제니까 규칙부터 찾아보기
import sys
input = sys.stdin.readline

n = int(input())

sum_list = [1, 2] * 501

for i in range(2, 1001):
    sum_list[i] = sum_list[i - 1] + sum_list[i -2]

print(sum_list[n - 1] % 10007)