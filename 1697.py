N, K = map(int, input().split())
time = 0
re = True
lst =[K]
while re:
    for i in lst:
        if i == N:
            re = False
        else:
            lst = [i+1, i-1]
            if i % 2 == 0:
                lst.append(i // 2)
 
    time += 1

print(time-1)
