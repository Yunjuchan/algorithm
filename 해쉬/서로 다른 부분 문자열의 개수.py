x = input()
N = len(x)
R = {}
for i in range(1, N+1):
    for j in range(0, N-i+1) :   
        R[x[j:j+i]] = R.get(x[j:j+i], 0) + 1
print(len(R.items()))