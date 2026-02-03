import sys
input = sys.stdin.readline

n = int(input())

queue = []

for _ in range(n):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == 'push':
        queue.append(command[1])
    elif cmd_type == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif cmd_type == 'size':
        print(len(queue))
    elif cmd_type == 'empty':
        print(1 if not queue else 0)
    elif cmd_type == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd_type == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])