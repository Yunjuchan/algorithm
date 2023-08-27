# '''
# 변신해서 워프했을 때 이동한 거리가 더 짧아야함
# 변신중에는 계속 워프 가능

# 십자가에 워프가 있는지 확인하면서 계속 이동
# 워프할 위치가 그냥 가는 것보다 빠르게 도착할 수 있어야 함
# 아마 bfs

# '''
# from collections import deque

# def bfs(y, x) :
#     que = deque()
#     que.append([y, x, 0]) # 레벨, 좌표, 모드
#     while que :
#         y, x , mode= que.popleft()
#         for i in range(4) :
#             dy, dx = y, x
#             for j in range(N) :
#                 flag = -1
#                 dy += direct_y[i]
#                 dx += direct_x[i]
#                 if 0 <= dy < N and 0 <= dx < N :
#                     if arr[dy][dx] == '#' :
#                         if mode == 0 and route[dy][dx] > route[y][x]+t+1 :
#                             route[dy][dx] = route[y][x]+t+1
#                             flag = 1
#                         elif mode == 1 and route[dy][dx] > route[y][x]+1 :
#                             route[dy][dx] = route[y][x]+1
#                             flag = 1 
#                     if route[dy][dx] > route[y][x]+j+1 :
#                         route[dy][dx] = route[y][x]+j+1
#                         flag = 0
#                 else :
#                     break

#                 if (flag == 0 and j == 0) or flag == 1:
#                     que.append([dy, dx, flag])

                
# direct_y = [0,0,1,-1]
# direct_x = [1,-1,0,0]
# N, t, t_y, t_x = map(int, input().split())
# t_y -= 1
# t_x -= 1
# route = [[i+j for j in range(N)] for i in range(N)] 
# arr = [list(input()) for _ in range(N)]
# bfs(0,0)
# print(route[t_y][t_x])
## 잠시 보류
