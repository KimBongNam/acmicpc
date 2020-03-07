import sys
M = int(input())
ans = set()
for i in range(M):
    lst = sys.stdin.readline().split()
    if len(lst) == 2:
        lst[1] = int(lst[1])
    if lst[0] == "add":
        ans.add(lst[1])
    elif lst[0] == "remove":
        if lst[1] in ans:
            ans.remove(lst[1])
    elif lst[0] == "check":
        print(1 if lst[1] in ans else 0)
    elif lst[0] == "toggle":
        if lst[1] in ans:
            ans.remove(lst[1])
        else:
            ans.add(lst[1])
    elif lst[0] == "all":
        ans = set(list(range(1,21)))
    elif lst[0] == "empty":
        ans = set()
    