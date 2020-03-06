import sys
import heapq
N = int(input())
13

lst = [int(sys.stdin.readline()) for _ in range(N)]


ans = []
for i in lst:
    if i == 0:
        print(0 if len(ans)==0 else heapq._heappop_max(ans))
    else:
        ans.append(i)
        heapq._heapify_max(ans)