import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1) :
    for j in range(M-1, -1, -1) :
        if arr[i][j] == 1 :
            cnt += 1
            for y in range(i+1) :
                for x in range(j+1) :
                    arr[y][x] += 1
                    arr[y][x] %= 2
print(cnt)