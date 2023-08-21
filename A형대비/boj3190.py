from collections import deque
direct_y = [0,1,0,-1]       # 우회전은 인덱스 + 1
direct_x = [1,0,-1,0]       # 좌회전은 인덱스 - 1
N = int(input())
arr = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K) :
    y, x = map(int, input().split())
    arr[y-1][x-1] = '#'

L = int(input())
com = deque()
for _ in range(L) :
    sec, c = input().split()
    com.append([int(sec), c])

cnt = 0
second = 0
bam = deque()
d = 0
bam.append([0,0])
arr[0][0] = 1
head_y = head_x = 0
while True :
    second += 1
    head_y += direct_y[d]
    head_x += direct_x[d]
    bam.append([head_y, head_x])
    if head_y >= N or head_y < 0 or head_x >= N or head_x < 0 :
       break
    elif arr[head_y][head_x] == 1 :
        break
    elif arr[head_y][head_x] == 0:
        y, x = bam.popleft()
        arr[y][x] = 0
    if com :
        if com[0][0] == second :
            sec, c = com.popleft()
            if c == 'L' :
                d -= 1
                d %= 4
            else :
                d += 1
                d %= 4
    arr[head_y][head_x] = 1
print(second)
        
