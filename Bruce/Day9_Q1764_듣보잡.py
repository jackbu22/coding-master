import sys

def solve():
    input = sys.stdin.readline

    N,M = map(int, input().split())
    Nolisten = set()
    Nosee = set()

    for _ in range(N):
        Name = sys.stdin.readline().strip()
        Nolisten.add(Name)

    for _ in range(M):
        Name = sys.stdin.readline().strip()
        Nosee.add(Name)
    
    result = list(Nolisten.intersection(Nosee))
    result.sort()

    print(len(result))

    for i in range(len(result)):
        print(result[i])



if __name__ == "__main__":
    solve()