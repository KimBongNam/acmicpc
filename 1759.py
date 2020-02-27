from itertools import combinations
L, C = map(int, input().split())
vowel = 'aeiou'
words = sorted(input().split())
pwd = list(map(''.join, combinations(words, L)))

for i in pwd:
    num_vow = 0
    for j in i:
        if j in vowel:
            num_vow += 1
    num_cons = L - num_vow

    if num_vow != 0 and num_cons >= 2:
        print(i)