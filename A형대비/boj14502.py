from collections import deque
import copy 
import sys
input = sys.stdin.readline
direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]
def abc(level, start) :        # 모든 경우의 수 구하기
    if level == 3 :
        x = copy.deepcopy(path)
        path_list.append(x)
        return
    for i in range(start,len(lst)) :
        if not visited[i] :
            visited[i] = True
            path.append(lst[i])
            abc(level+1, i+1)
            visited[i] = False
            path.pop()

def bfs(a) :         # 바이러스 퍼트리기
    global Min
    que2 = copy.deepcopy(que)
    cnt = len(que2)
    while que2 :
        if cnt > Min :
            return 
        y, x = que2.popleft()
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if a[dy][dx] == 0 :
                    
                    a[dy][dx] = 2
                    que2.append([dy, dx])
                    cnt += 1

def count() :           # 물들여진 구역 구하기
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if arr2[i][j] == 2 :
                cnt += 1
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []        # 0인 위치 저장 배열
que = deque()   # 2인 위치 저장 배열
Min = 21e8
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 0 :
            lst.append([i, j])
        elif arr[i][j] == 2 :
            que.append([i, j])
visited = [False] * len(lst)
path_list = []
path = []

abc(0,0)

for path in path_list :
    arr2 = copy.deepcopy(arr)
    for y, x in path :
        arr2[y][x] = 1
    bfs(arr2)
    cnt = count()
    
    if cnt < Min :
        min_path = copy.deepcopy(path)
        Min = cnt

for y, x in min_path :
    arr[y][x] = 1

bfs(arr)

cnt_s = 0
for i in range(N) : 
    for j in range(M) :
        if arr[i][j] == 0 :
            cnt_s += 1

print(cnt_s)

