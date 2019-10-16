num = input()

real_num = 0
for i, word in enumerate(num):
    val = (8 ** i) * int(word)
    real_num = real_num + val
