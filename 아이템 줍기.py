from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    que = deque()
    que.append([0, characterY, characterX])
    direct_y = [1,0,-1,0,1,1,-1,-1]
    direct_x = [0,1,0,-1,1,-1,1,-1]
    arr = [[0]*51 for _ in range(51)]
    visited = [[False]*51 for _ in range(51)]
    visited[characterY][characterX] = True
    
    for x1, y1, x2, y2 in rectangle :
        for i in range(y1, y2+1) :
            for j in range(x1, x2+1) :
                arr[i][j] = 1
                if i != y2 and j != x2 :
                    box[i][j] = 1
    box = [[0]*51 for _ in range(51)]
    while que :
        level, y, x = que.popleft()
        visited[y][x] = True
        flag = 0
        tmp = []
        for i in range(8) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if i >= 4 :
                if arr[dy][dx] == 1 :
                    flag += 1
                continue
            if dy < 0 or dy >= 50 or dx < 0 or dx >= 50 :
                continue
            if arr[dy][dx] == 1 :
                if visited[dy][dx] : continue

                tmp.append([level+1, dy, dx])
                if dx == itemX and dy == itemY :

                    return level
        if 0 < flag < 8 : 
            print(tmp)
            que += tmp
                
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	
characterX = 1	
characterY = 3	
itemX = 7
itemY = 8
print(solution(rectangle, characterX, characterY, itemX, itemY))