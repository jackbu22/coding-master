import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    Each = list(map(int, input().split()))

    Each.sort()

    time = 0
    total = []
    for i in range(N):
        time = time+Each[i]
        total.append(time)
        

    print(sum(total))
    



if __name__ == "__main__":
    solve()