import sys

def solve():
    input = sys.stdin.readline

    N = int(input())
    stack = []

    for i in range(N):
        func = input().split()
        if func[0] == "push":
            stack.append(int(func[1]))

        elif func[0] == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())

        elif func[0] == "size":
            print(len(stack))

        elif func[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        elif func[0] == "top" :
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])



    


if __name__ == "__main__":
    solve()