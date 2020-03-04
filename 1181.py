import sys
N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
word = sorted(list(set(words)))
ans = sorted(word, key = lambda x: len(x))
for i in ans:
    print(i)