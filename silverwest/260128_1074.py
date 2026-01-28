import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def find_2(n): # 가장 가까운 2의 제곱수(나중에 나머지 구할라고)
    if n == 0:
        return 0
    return 1 << (n.bit_length() - 1)

def find_s(n): # 가장 가까운 2의 제곱수의 지수 구하기(반씩 나눈거 몇번인지 볼라고)
    if n == 0:
        return None
    return n.bit_length() - 1


## 가로 세로 기준 반씩 나눠서 하면 될 듯도 한데....