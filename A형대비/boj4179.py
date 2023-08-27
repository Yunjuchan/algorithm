from collections import deque
import sys
input = sys.stdin.readline
direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]
# def bfs1(y, x) :
#     que = deque()
#     que.append([y, x, 0])
#     route[y][x] = 0
#     while que :
#         y, x, level = que.popleft()
#         for i in range(4) :
#             dy = direct_y[i] + y
#             dx = direct_x[i] + x
#             if 0 <= dy < N and 0 <= dx < M :
#                 if arr[dy][dx] != '#' and (route[dy][dx] == -1 or route[dy][dx] > level+1):
#                     route[dy][dx] = level+1
#                     que.append([dy, dx, level+1])

# def bfs2(y, x) :
#     que = deque()
#     que.append([y, x, 0])
#     while que :
#         y, x, level = que.popleft()
#         for i in range(4) :
#             dy = direct_y[i] + y
#             dx = direct_x[i] + x
#             if 0 <= dy < N and 0 <= dx < M :
#                 if arr[dy][dx] != '#' and route[dy][dx] > level:
#                     route[dy][dx] = level+1
#                     que.append([dy, dx, level+1])
#             else :
#                 return level+1
#     return -1

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
que = deque()
level = 0
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'F' :
            que.append(['F', i, j, level])
        elif arr[i][j] == 'J' :
            que.appendleft(['J', i, j, level])

flag = 0
while que :
    tp, y, x, level = que.popleft()
    if tp == 'J' :
        if arr[y][x] == 'F' :
            continue
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if arr[dy][dx] == '.' :
                    arr[dy][dx] = 'J'
                    que.append([tp, dy, dx, level + 1])
            else :
                flag = 1
                break
        if flag == 1 :
            break
    elif tp == 'F' :
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if 0 <= dy < N and 0 <= dx < M :
                if arr[dy][dx] != '#' and arr[dy][dx] != 'F':
                    arr[dy][dx] = tp
                    que.append([tp, dy, dx, level + 1])

if flag == 1 :
    print(level+1)
else :
    print('IMPOSSIBLE')   