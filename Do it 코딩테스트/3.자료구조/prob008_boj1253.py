import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
X.sort()
cnt = 0
for i in range(len(X)) :
    idx1 = 0 
    idx2 = N-1
    while idx1 < idx2 :
        if X[idx1] + X[idx2] > X[i] or i == idx2:
            idx2 -= 1
        elif X[idx1] + X[idx2] < X[i] or i == idx1 :
            idx1 += 1
        else :
            cnt += 1
            break
print(cnt)
    