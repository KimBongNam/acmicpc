per = []
def permutation(per, N):
    for i in range(1,N+1):
        per.append(permutation(per, N-1))
        return per
print(permutation(per, 3))
        