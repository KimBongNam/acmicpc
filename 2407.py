def factorial(num, end):
    if num == end:
        return end
    else:
        return num * factorial(num-1, end)

n, m = map(int, input().split())
print(factorial(n,n-m+1) // factorial(m,1))