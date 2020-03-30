A, B = map(int, input().split())

m = int(input())

lst = list(map(int, input().split()))

origin = 0
for i in range(m):
    origin += (A ** i) * lst[m-i-1]

ans = []
if origin < B:
    print(origin)
else:
    while origin >= B:
        x, y = divmod(origin, B)
        ans.append(y)
        origin = x
    print(x, *reversed(ans))

