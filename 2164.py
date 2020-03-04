from collections import deque

N = int(input())
6
card = deque([i+1 for i in range(N)])
while len(card) != 1:
    card.popleft()
    
    card.rotate(-1)

print(*card)