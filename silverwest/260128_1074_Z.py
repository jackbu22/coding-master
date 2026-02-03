import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

result = []                         # 몇 사분면 좌표인지 계속 쌓는 리스트
cnt = 0

def solve(x, y, size):
    if size == 1:                   # 자기 자신의 좌표가 되면 끝
        return

    half = size // 2

    if x < half and y < half:       # 1사분면은 앞에 굳이 더할 거 없음-> 0
        result.append(0)
        solve(x, y, half)           # 다시 4등분 재귀

    elif x >= half and y < half:
        result.append(1)
        solve(x - half, y, half)    # x에서 half 빼서 1사분면으로 만들어주고 재귀

    elif x < half and y >= half:
        result.append(2)
        solve(x, y - half, half)    

    else:
        result.append(3)
        solve(x - half, y - half, half)

solve(c, r, 2 ** n)

for i in range(len(result)):
    cnt += result[-(i + 1)] * (2 ** (2 * i))    # 가장 최근에 알게된 사분면부터 카운트 세주기

print(cnt)

