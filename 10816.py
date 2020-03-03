N = int(input())
having = list(map(int, input().split()))
d = {}
for i in having:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
M = int(input())
question = list(map(int, input().split()))

for i in question:
    if i in d:
        print(d[i], end=' ')
    else:
        print(0, end=' ')