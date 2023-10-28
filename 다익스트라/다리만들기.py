from collections import deque
import sys
input = sys.stdin.readline
N = int(input().rstrip())
# 입력받은 섬 상태
island = [list(map(int, input().split())) for _ in range(N)]

# 섬과 섬 사이의 거리 배열
island2 = [[21e8]*N for _ in range(N)]

direct_y = [1,0,-1,0]
direct_x = [0,1,0,-1]
que2 = deque() # bfs 돌리기 위한 변수 check함수에서 que를 쓰기 때문에 다른 변수 할당
cnt = 1     # 몇번째 섬인지 체크하는 변수

# 몇번째 섬인지 체크
def check(idx, y, x) :
    que = deque()
    que.append((y, x))
    while que :
        flag = 1
        y, x = que.popleft()
        island2[y][x] = 0   # 입력받은 값이 1이면 이동거리를 0으로 바꿈
        for i in range(4) :
            dy = direct_y[i] + y
            dx = direct_x[i] + x
            if dy < 0 or dx < 0 or dy >= N or dx >= N : continue

            if island[dy][dx] == 1 :    # 인접한 땅이 1이면 계속 땅 갱신
                que.append((dy, dx))
                island[dy][dx] = -idx   # 땅의 번호로 갱신 1로하면 다시 찾아버리기때문에 일부러 음수 붙혀줌
            elif island[dy][dx] == 0 :  
                flag = 0                # que2에 여러번 들어가는 것 방지하기 위해서 flag 변수 둬야함
        if flag == 0 :
            que2.append((-idx, y, x))
                
# 땅 구분하기
for i in range(N) :
    for j in range(N) :
        if island[i][j] != 1 : continue
        island[i][j] = -cnt
        check(cnt, i, j)
        cnt += 1

# 다리 만들기
ret = 21e8
while que2 :
    tp, y, x = que2.popleft()   # 땅의 번호, y,x좌표
    for i in range(4) :
        dy = direct_y[i] + y
        dx = direct_x[i] + x
        if dy < 0 or dx < 0 or dy >= N or dx >= N : continue

        if island2[dy][dx] == 21e8 :    # 한번도 지나지 않은 땅이라면 
            island[dy][dx] = tp         # 어떤땅인지 체크해주고
            island2[dy][dx] = island2[y][x] + 1 # 거리 체크
            que2.append((tp, dy, dx))   
        else :
            if island[dy][dx] == tp : continue  # 같은 땅에 도착했으면 거리 계산 필요 x
            if ret > island2[dy][dx] + island2[y][x] :  # 만약에 다른 땅이라면 최솟값 갱신
                ret = island2[dy][dx] + island2[y][x]

print(ret)