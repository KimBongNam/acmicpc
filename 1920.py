N = int(input()) # 10^5
Alst = list(map(int, input().split()))
M = int(input()) # 10^5
Blst = list(map(int, input().split()))

Alst.sort()
for i in Blst:
    low = 0
    high = len(Alst)-1
    while low <= high:
        mid = (low + high) // 2
        if Alst[mid] > i:
            high = mid - 1
        elif Alst[mid] < i:
            low = mid + 1
        else:
            low = high+1
    
    if Alst[mid] == i:
        print(1)
    else:
        print(0)