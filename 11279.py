import sys
import heapq

def heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap,0,len(heap)-1)

N = int(input())
13
lst = [int(sys.stdin.readline()) for _ in range(N)]
0
1
2
0
0
3
2
1
0
0
0
0
0

ans = []
for i in lst:
    if i == 0:
        print(0 if len(ans)==0 else heapq._heappop_max(ans))
    else:
        heappush_max(ans, i)
