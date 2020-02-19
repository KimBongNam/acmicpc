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
if M != 10:
    mini = ''
    for i in N:
        if int(i) in usable:
            mini += i
        else:
            if len(usable) != 0:
                mini += str(usable[-1]) * (len(N)-len(mini))
            else:
                mini = answer
            break
    maxi = ''
    for i in N:
        if int(i) in usable:
            maxi += i
        else:
            if len(usable) != 0:
                maxi += str(usable[0]) * (len(N)-len(maxi))
            else:
                maxi = answer
            break
else:
    mini = '99999999'
    maxi = '99999999'
print((answer, abs(int(mini)-int(N))+len(mini)-1, abs(int(maxi)-int(N))+len(maxi)-1))
print(min(answer, abs(int(mini)-int(N))+len(mini), abs(int(maxi)-int(N))+len(maxi)))
