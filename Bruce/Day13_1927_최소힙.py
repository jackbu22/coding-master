import sys
import heapq

def solve():

    input = sys.stdin.readline
    N = int(input())

    heap = []
    for i in range(N):
        x = int(input())
        if x!=0:
            heapq.heappush(heap,x)
        
        elif x==0:
            if len(heap) ==0:
                print(0)
            else:
                heapq.heappop(heap)

    

if __name__ == "__main__":                              
    solve()