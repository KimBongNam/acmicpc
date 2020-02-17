N = input()
M = int(input())
broken = []
if M:
    broken.extend(input().split())
current = 100
usable = []
for i in range(10):
    if str(i) not in broken:
        usable.append(i)
answer = abs(int(N)-100)
mini = ''
for i in N:
    if int(i) in usable:
        mini += i
    else:
        mini += str(usable[-1]) * (len(N)-len(mini))
        break
maxi = ''
for i in N:
    if int(i) in usable:
        maxi += i
    else:
        maxi += str(usable[0]) * (len(N)-len(maxi))
        break
print(min(answer, abs(int(mini)-int(N))+len(mini), abs(int(maxi)-int(N))+len(maxi)))