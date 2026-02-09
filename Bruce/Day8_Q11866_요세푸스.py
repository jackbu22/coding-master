import sys
import queue

from collections import deque

def solve():

    input = sys.stdin.readline
    N, k = map(int, input().split())

    ns = []
    for i in range(N):
        ns.append(i+1)
    
    ns = deque(ns)
    print('<', end="")
    for i in range(N):
        if len(ns)>k:
            if len(ns) ==1:
                print(ns[k-1], end="")
            else:
                print(ns[k-1], end=", ")
            del ns[k-1]
            ns.rotate(N-k-i)

        
        elif len(ns) ==k:
            if len(ns) ==1:
                print(ns[k-1], end="")
            else:
                print(ns[k-1], end=", ")
            del ns[k-1]

        elif len(ns) < k:
            nss=ns.copy()
            while len(nss) < k:
                nss= nss+ns
            if len(ns) != 1:
                print(nss[k-1], end=", ")
            else:
                print(nss[k-1], end="")
            index = ns.index(nss[k-1])
            del ns[index]
            if index != 0:
                ns.rotate(len(nss)-k)



    print('>')

    


if __name__ == "__main__":                              
    solve()