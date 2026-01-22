import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ghs = list(input().strip())
    stack = []
    for gh in ghs:
        if gh == '(':
            stack.append(gh)
        else:
            if len(stack) >= 1 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(gh)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


    