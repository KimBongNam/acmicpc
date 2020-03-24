import sys
import statistics
from collections import Counter
N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
print(round(statistics.mean(lst)))
print(statistics.median(lst))
a = Counter(lst).most_common()
val = a[0][1]
of = []
for i in a:
    if i[1]==val:
        of.append(i)
of.sort(key=lambda x:x[0])
print(of[0][0] if len(of)==1 else of[1][0])
print(max(lst)-min(lst))