n = int(input())
word = input()

sum = 0
for i, string in enumerate(word):
    sum += ((ord(string)-96) * (31**i)) % 1234567891

print(sum)