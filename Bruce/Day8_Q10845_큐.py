import sys
import queue

def solve():
    input = sys.stdin.readline

    N = int(input())
    que = queue.Queue()

    for i in range(N):
        func = input().split()
        if func[0] == "push":
            que.put(int(func[1]))

        elif func[0] == "pop":
            if que.empty()==True:
                print(-1)
            else:
                print(que.get())

        elif func[0] == "size":
            print(que.qsize())

        elif func[0] == "empty":
            if que.empty()==True:
                print(1)
            else:
                print(0)

        elif func[0] == "front" :
            if que.empty()==True:
                print(-1)
            else:
                print(que.queue[0])

        elif func[0] == "back" :
            if que.empty()==True:
                print(-1)
            else:
                print(que.queue[-1])



    


if __name__ == "__main__":
    solve()