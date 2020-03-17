import sys
N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(input())
for i in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        numbers[query[1]-1] = query[2]
    else:
        print(numbers.index(min(numbers))+1)