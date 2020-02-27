A, B = map(int, input().split())

mini = 1

for i in range(1,min(A, B)+1):
    if A % i == 0 and B % i == 0:
        mini = i

lst1 = []
lst2 = []

found = True
i = 1
while found:
    low = min(A,B)
    high = max(A,B)
    lst1.append(low*i)
    lst2.append(high*i)
    if lst1[i-1] in lst2:
        found = False
        maxi = lst1[i-1]
    i += 1
print(mini)
print(maxi)
