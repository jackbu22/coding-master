import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    comm = int(input())
    if comm == 0 :
        if len(heap) > 0:
            min_val = heapq.heappop(heap)
            print(min_val)
        else:
            print(0)

    else:
        heapq.heappush(heap, comm)
