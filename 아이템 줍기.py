from collections import deque

# def solution(rectangle, characterX, characterY, itemX, itemY):
#     def is_edge(x, y, i) :
#         dy = direct_y[i] + y
#         dx = direct_x[i] + x
#         if arr[dy][dx] == 0 :
#             return 1
#         return 0
#     que = deque()
#     que.append([0, characterY, characterX])
#     direct_y = [1,0,-1,0,1,1,-1,-1]
#     direct_x = [0,1,0,-1,1,-1,1,-1]
#     arr = [[0]*51 for _ in range(51)]
#     visited = [[False]*51 for _ in range(51)]
#     visited[characterY][characterX] = True
    
#     for x1, y1, x2, y2 in rectangle :
#         for i in range(y1, y2+1) :
#             for j in range(x1, x2+1) :
#                 arr[i][j] = 1

#     while que :
#         level, y, x = que.popleft()
#         visited[y][x] = True
#         for i in range(4) :
#             dy = direct_y[i] + y
#             dx = direct_x[i] + x
        
#             if dy < 0 or dy >= 50 or dx < 0 or dx >= 50 :
#                 continue
#             if arr[dy][dx] == 1 :
#                 if visited[dy][dx] : continue

