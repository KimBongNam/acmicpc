import sys

P, V = map(int, input().split())
lst = [sys.stdin.readline().split() for _ in range(P)]

local = {}
prop=  {}
for i in range(P):
    lst[i][1] = int(lst[i][1])
    lst[i][2] = int(lst[i][2])
    local[lst[i][0]] = lst[i][1]
    prop[lst[i][0]] = lst[i][2]

N = 300
valid = sum([lst[i][2] for i in range(P)])  
assign = [lst[i][0] for i in range(P) if (lst[i][2]/valid) >= 0.03 or lst[i][1] >= 5]
R = 253 - sum([local[i] for i in assign])
p = {}
r = {}
prop_sum = sum([prop[i] for i in assign])
for i in assign:
    p[i] = prop[i] / prop_sum
    r[i] = local[i]

s = {}
for i in p:
    val = ((N-R)*p[i]-r[i])/2
    if val < 1:
        s[i] = 0
    else:
        s[i] = round(val)
comp = sum(s.values())

if comp < 30:
    q = {}
    for j in assign:
        q[j] = s[j] + (30-comp)*p[j]
        s[j] = int(q[j])
        q[j] -= s[j]
    qlst = list(q.keys())
    qlst.sort(key = lambda x: q[x], reverse=True)
    comp = sum(s.values())
    cnt = 0
    while comp < 30:
        s[qlst[cnt]] += 1
        cnt = (cnt + 1) % len(assign)
        comp += 1
elif comp > 30:
    q = {}
    for j in assign:
        q[j] = (30 * s[j]) / comp
        s[j] = int(q[j])
        q[j] -= s[j]
    comp = sum(s.values())
    qlst = list(q.keys())
    qlst.sort(key = lambda x: q[x], reverse=True)
    cnt = 0
    while comp < 30:
        s[qlst[cnt]] += 1
        comp += 1
        cnt = (cnt+1) % len(assign)

third = {}
t = {}
for j in assign:
    third[j] = (17 * p[j])
    t[j] = int(third[j])
    third[j] -= t[j]

comp = sum(t.values())
tlst = list(third.keys())
tlst.sort(key = lambda x: third[x], reverse=True)
cnt = 0
while comp < 17:
    t[tlst[cnt]] += 1
    comp += 1
    cnt = (cnt+1) % len(assign)

final = {}
for i in local:
    a, b, c= 0,0,0
    if r.get(i):
        a = r.get(i)
    if s.get(i):
        b = s.get(i)
    if t.get(i):
        c = t.get(i)
    final[i] = a + b + c
flst = list(final.keys())
flst.sort()
flst.sort(key = lambda x: final[x], reverse=True)
for i in flst:
    print(i, final[i])