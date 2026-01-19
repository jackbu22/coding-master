import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ghs = list(input().strip())
    stack = []
    for gh in ghs:
        stack.append(gh)
        if gh == ')':
            if len(stack) >= 2 and stack[-2] == '(':
                stack.pop()
                stack.pop()
            else:
                stack.append(gh)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


    