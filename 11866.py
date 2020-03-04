N, K = map(int, input().split())

ans = []
lst = [i+1 for i in range(N)]
i = K-1
while len(lst) !=  1:
    ans.append(lst[i])
    del lst[i]
    i = i+K-1 if i+K-1 < len(lst) else (i+K-1)%len(lst)

ans.append(lst[0])

print("<", end='')
for i in range(len(ans)-1):
    print("{}, ".format(ans[i]), end='')
print("{}>".format(ans[-1]))