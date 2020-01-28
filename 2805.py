N, M = map(int, input().split())
lst = list(map(int,input().split()))
low = 0
high = max(lst)
height = 0
while low <= high:
    length = 0
    mid = (low+high)//2
    for i in lst:
        if i-mid > 0:
            length += i - mid
    if length >=M:
        height = mid
        low = mid + 1
    if length < M:
        high = mid - 1

print(height)