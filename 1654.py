import sys
K, N = map(int, input().split())
lst = list(map(int, sys.stdin.readlines()))

low = 1
high = max(lst)
ans = 0
while low <= high:
    count = 0
    mid = (low + high)//2
    for i in lst:
        val = i // mid
        count += val
    if count >= N:
        if ans < mid:
            ans = mid
        low = mid + 1
    elif count < N:
        high = mid - 1
print(ans)