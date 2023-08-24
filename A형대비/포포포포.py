'''
catch : 포가 먹은 졸들을 저장해주는 변수 나중에 중복 제거

메커니즘  
다이렉트 방향으로 가다가 졸이 있으면 뛰어넘고 다음부터 한칸씩 dfs실행
그다음 졸을 만나면 먹어버림 catch에 저장 그 위치에서도 다시 dfs실행

붙어있을 때 안됨
벽을 만나면 안됨 
visited는 필요없음
졸이 사라졌다 생겼다 해야하는데 이거 처리할 방법 생각

'''

direct_y = [0,0,1,-1]
direct_x = [1,-1,0,0]

def dfs(y, x, level) :
    global result
    if level == 3 :
        if catch :
            for i in catch :
                if i not in result :
                    result.append(i)
        return
    
    for j in range(4) :
        flag = 0                # 졸 넘었다 표시
        for i in range(1, N) :
            dy = direct_y[j]*i + y
            dx = direct_x[j]*i + x
            if 0 <= dy < N and 0 <= dx < N :
                if flag == 0 :  # 졸을 아직 안넘었을 때
                    if arr[dy][dx] == 1 :  # 만나면 넘었다는 표시
                        flag = 1
                else :  # 졸 하나를 넘었을 때
                    if arr[dy][dx] == 1 :
                        arr[dy][dx] = 0
                        catch.append([dy,dx])
                        dfs(dy, dx, level+1)
                        dy, dx = catch.pop()
                        arr[dy][dx] = 1
                        break
                    else :
                        dfs(dy, dx, level+1)
            else :
                break

                    
T = int(input())
for tc in range(1, T+1) :
    catch = []
    result  = []
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 2 :
                dfs(i,j, 0)
    result.sort()
    print(result)
    print(f'#{tc} {len(result)}')