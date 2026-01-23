import sys
input = sys.stdin.readline

m = int(input())

ex_set = set()
full_set = set(str(i) for i in range(1, 21))

for _ in range(m):
    command = input().split()
    cmd_type = command[0]

    if cmd_type == 'all':
        ex_set = full_set.copy()
    elif cmd_type == 'empty':
        ex_set.clear()
    else:
        value = command[1]
        if cmd_type == 'add':
            ex_set.add(value)
        elif cmd_type == 'remove':
            ex_set.discard(value)
        elif cmd_type == 'check':
            if value in ex_set:
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif cmd_type == 'toggle':
            if value in ex_set:
                ex_set.remove(value)
            else:
                ex_set.add(value)


    


