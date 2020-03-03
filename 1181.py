import sys
N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
words.sort()
for i in words:
    print(i)