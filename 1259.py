import sys
lst = list(map(str, sys.stdin.readlines()))

def pelindrome(string):
    print(string)
    if len(string) == 0 or len(string) == 1:
        return 'yes'
    elif string[0] == string[-2]:
        return pelindrome(string[1:-2])
    else:
        return 'no'
for i in lst[:-1]:
    ans = pelindrome(i)
    print(ans)