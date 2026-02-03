import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = set(input().strip() for i in range(n))
see = set(input().strip() for i in range(m))


l_s = listen & see

print(len(l_s))
print('\n'.join(i for i in sorted(l_s)))