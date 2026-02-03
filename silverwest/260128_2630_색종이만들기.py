import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt_w = 0
cnt_b = 0

def solve(x, y, size):
    global cnt_w, cnt_b

    first = paper[x][y] # 기준 좌표
    same = True   # 일단 내부가 같다고 가정하고

    for i in range(x, x + size):      #첫번째부터 사이즈 끝까지
        for j in range(y, y + size):
            if paper[i][j] != first:  # 사각형 안에서 하나라도 다르다면
                same = False          # 내부가 다름을 확인함
                break
        if not same:                  # 내부가 다르다면 반복문 나오기
            break

    if same:                          # 내부가 다 같은 걸 확인하면
        if first == 0:
            cnt_w += 1
        else:
            cnt_b += 1
        return

    half = size // 2                  # 사이즈 반으로 줄여주고
    solve(x, y, half)                 # 왼쪽 위
    solve(x, y + half, half)          # 오른쪽 위
    solve(x + half, y, half)          # 왼쪽 아래
    solve(x + half, y + half, half)   # 오른쪽 아래

solve(0, 0, n)

print(cnt_w)
print(cnt_b)
