import sys
from typing import Counter

from collections import Counter

def solve():
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    A_count = Counter(A)

    M = int(input())
    B = list(map(int, input().split()))

    for x in B:
        print(A_count[x], end=" ")


if __name__ == "__main__":
    solve()