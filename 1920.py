N = int(input()) # 10^5
Alst = list(map(int, input().split()))
M = int(input()) # 10^5
Blst = list(map(int, input().split()))

Alst.sort()
for i in Blst:
    low = 0
    high = len(Alst)-1
    find = False
    while low <= high and not find:
        mid = (low + high) // 2
        if Alst[mid] > i:
            low += 1
        elif Alst[mid] < i:
            high -= 1
        else:
            print(1)
            find = True
            
    if not find:
        print(0)