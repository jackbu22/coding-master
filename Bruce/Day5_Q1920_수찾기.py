import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    A = set(map(int, input().split()))

    M = int(input())
    B = list(map(int, input().split()))

    result = []

    for x in B:
        if x in A:
            result.append("1")
        else:
            result.append("0")

    print("\n".join(result))


if __name__ == "__main__":
    solve()