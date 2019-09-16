import sys

inp = sys.stdin.readlines()
inp_1 = list(map(int,inp[0].split()))
card = list(map(int,inp[1].split()))

answer = -1
for i in range(len(card)):
    for j in range(i+1,len(card)-1):
        for k in range(j+1, len(card)):
            if card[i]+card[j]+card[k] > inp_1[1]:
                pass
            elif card[i]+card[j]+card[k] > answer:
                answer = card[i]+card[j]+card[k]
print(answer)
