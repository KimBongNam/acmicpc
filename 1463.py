num = int(input())
lst = [-1]*1000000
def f(n):
    if n==1: return 1
    if n==2: return 1
    if n==3: return 1
    if lst[int(n)] != -1: return lst[int(n)]
    if n%3 == 0:
        lst[int(n)] = min(f(n/3),f(n-1))+1
        return lst[int(n)]
    elif n%2 == 0:
        lst[int(n)] = min(f(n/2), f(n-1)) +1
        return lst[int(n)]
    else:
        lst[int(n)] = f(n-1)+1
        return lst[int(n)]

print(f(num))
