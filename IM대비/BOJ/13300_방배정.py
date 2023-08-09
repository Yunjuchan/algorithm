import sys
input = sys.stdin.readline
N, K  = map(int, input().split())
arr = [[0] * 6 for _ in range(2)]
for i in range(N) :
    s, grade = map(int, input().split())
    arr[s][grade-1] += 1
room = 0
for i in range(2) :
    for j in range(6) :
        room += arr[i][j] // K
        if arr[i][j] % K != 0 :
            room += 1
print(room)