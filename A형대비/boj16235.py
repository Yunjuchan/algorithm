from collections import deque
import sys
input = sys.stdin.readline

direct_y = [0,0,-1,1,-1,-1,1,1]
direct_x = [1,-1,0,0,1,-1,1,-1]
N, M, K = map(int, input().split())
fert = [[5]*N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
forest = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M) :
    y, x, z = map(int, input().split())
    forest[y-1][x-1].append(z)

def ss() :
    for i in range(N) :
        for j in range(N) :
            if forest[i][j] :
                tmp = deque()
                dead = 0
                for tree in forest[i][j] :
                    if fert[i][j] >= tree :
                        tmp.append(tree+1)
                        fert[i][j] -= tree
                    else : dead += tree // 2
                forest[i][j] = tmp
                fert[i][j] += dead

def fw() :
    for i in range(N) :
        for j in range(N) :
            fert[i][j] += arr[i][j] 
            if forest[i][j] :
                for tree in forest[i][j] :
                    if tree % 5 == 0 :
                        for k in range(8) :
                            dy = direct_y[k] + i
                            dx = direct_x[k] + j
                            if 0 <= dy < N and 0 <= dx < N :
                                forest[dy][dx].appendleft(1)

cnt = 0
for _ in range(K) :
    ss()
    fw()

for i in range(N) :
    for j in range(N) :
        cnt += len(forest[i][j])
print(cnt)