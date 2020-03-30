import sys

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    print("E" if n % 2 == 1 else 'O')

    짝수 >= 홀수 O 
    1 E 2 O 3 E 4 O