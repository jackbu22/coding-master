import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(list(input().strip()))

counts = []

for i in range(n - 7):
    for j in range(m - 7):
        cnt_1 = 0 
        cnt_2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt_1 += 1
                    if board[a][b] != 'B':
                        cnt_2 += 1
                else:
                    if board[a][b] != 'B':
                        cnt_1 += 1
                    if board[a][b] != 'W':
                        cnt_2 += 1
        
        
        counts.append(cnt_1)
        counts.append(cnt_2)


print(min(counts))