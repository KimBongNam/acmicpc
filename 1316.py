import sys
N = int(input())

cnt = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    dic = {}
    for i,c in enumerate(word):
        if not dic.get(c):
            dic[c] = 1
        else:
            dic[c] += 1

        if dic.get(c)>1:
            if word[i-1] != c:
                dic[c]-=1
                break
        
    sum = 0
    for i in dic:
        sum += dic[i]
    if sum == len(word):
        cnt += 1

print(cnt)
