import sys
N = input()
resul = list(map(str, sys.stdin.readlines()))

for res in resul:
    ans = 0
    score = 1
    for i in res:
        if i == "O":
            ans += score
            score += 1
        else:
            score = 1

    print(ans)