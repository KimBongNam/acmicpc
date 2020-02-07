E, S, M = map(int, input().split())
year = 1
EE = 1
SS = 1
MM = 1
find = E==EE and S==SS and M==MM

while not find:

    if EE <15:
        EE += 1
    else:
        EE = 1
    if SS < 28:
        SS += 1
    else:
        SS = 1
    if MM < 19:
        MM += 1
    else:
        MM = 1
    year += 1
    
    if E==EE and S==SS and M==MM:
        find = True
print(year)