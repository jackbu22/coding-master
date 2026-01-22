import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == 'push':
        stack.append(command[1])
    elif cmd_type == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd_type == 'size':
        print(len(stack))
    elif cmd_type == 'empty':
        print(1 if not stack else 0)
    elif cmd_type == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])