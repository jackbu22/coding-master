import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    
    coordinate = []
    for _ in range(N):
        x, y = map(int, input().split())
        coordinate.append((x, y))
    
    coordinate.sort()
    
    for x, y in coordinate:
        print(x, y)


if __name__ == "__main__":
    solve()
