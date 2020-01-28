import sys
N, C = map(int, input().split())
lst = list(map(int, sys.stdin.readlines()))
lst.sort()
low = 1
high = lst[-1]
ans = 0
while low <= high:
    possible = True
    mid = (low + high) // 2
    
    print(low, high, mid)
    for i in range(N-1):
        if abs(lst[i]-lst[i+1]) > mid:
            possible = False
        print(possible)
    if possible:
        if mid > ans:
            ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)

