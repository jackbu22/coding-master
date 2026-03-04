from collections import deque

import sys

def solve():
    input = sys.stdin.readline
    a,b = map(int, input().split())

    q = deque()
    q.append(a)
    visited = [False]*100001
    visited[a] =  0

    if a==b:
        print(0)
    elif a>b:
        print(a-b)
    else:

        while True:
            x = q.popleft()         #5
            i = visited[x]        #0
            if x+1 <= 100000:
                if visited[x+1] == False:
                    q.append(x+1)
                    visited[x+1] = i+1
                    if x+1 == b:
                        break
            if x-1 >=0:
                if visited[x-1] == False:
                    q.append(x-1)
                    visited[x-1] = i+1
                    if x-1 == b:
                        break
            if 2*x <= 100000:
                if visited[2*x] == False:
                    q.append(2*x)
                    visited[2*x] = i+1
                    if 2*x == b:
                        break

        print(visited[b])

if __name__ == "__main__":                              
    solve()