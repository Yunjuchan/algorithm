import sys
input = sys.stdin.readline
def draw(n1, n2) :
    for i in range(n1, n1+10) :
        for j in range(n2, n2+10) :
            arr[i][j] += 1
N = int(input())
arr = [[0] * 100 for _ in range(100)] 
cnt = 0
for i in range(N) :
    draw(*map(int, input().split()))
for y in range(100) :
    for x in range(100) :
        if arr[y][x] > 0 :
            cnt += 1
print(cnt)