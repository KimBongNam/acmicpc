N = input()
M = int(input())
broken = []
if M:
    broken.extend([input().split()])
current = 100
usable = []
for i in range(10):
    if str(i) not in broken:
        usable.append(i)
min = ''
for i in N:
    