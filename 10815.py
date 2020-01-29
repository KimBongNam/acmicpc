import sys
N = int(input())
hand_card = list(map(int, input().split()))
M = int(input())
find_card = list(map(int, input().split()))

hand_card.sort()


for card in find_card:
    low = 0
    high = N-1
    find = True
    while low <= high:
        mid = (low + high) // 2
        if hand_card[mid] == card:
            print(1, end = ' ')
            low = 1
            high = 0
            find = False
        elif hand_card[mid] < card:
            low = mid + 1
        else:
            high = mid - 1
    if find:
        print(0, end = ' ')