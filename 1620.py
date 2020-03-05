import sys
from string import ascii_uppercase
N, M = map(int, input().split())
monster = {}
num = {}
for i in range(1, N+1):
    val = sys.stdin.readline().strip()
    monster[val] = i
    num[i] = val
for i in range(M):
    question = sys.stdin.readline().strip()
    if question[0] in ascii_uppercase:
        print(monster.get(question))
    else:
        print(num.get(int(question)))