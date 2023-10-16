import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

k = 0
while True :
    if 2 ** k >= N :
        break
    k += 1
a = 2 ** k
arr = [0] * (2*a)
for i in range(N) :
    arr[i+a] = int(input().strip())

def setTree() :
    for i in range(2*a-1, 1, -1) :
        arr[i//2] += arr[i]

def chageVal(start, x) :
    d = x - arr[start]
    while start > 0 :
        arr[start] += d
        start //= 2

def getSum(start, end) :
    Sum = 0
    while start <= end :
        if start % 2 == 1 :
            Sum += arr[start]
        start += 1
        if end % 2 == 0 :
            Sum += arr[end]
        end -= 1
        start //= 2
        end //= 2
    return Sum 

setTree()

for _ in range(M+K) :
    x, y, z = list(map(int, input().split()))
    if x == 1 :
        chageVal(y+a-1, z)
    else :
        print(getSum(y+a-1, z+a-1))


