from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
que = deque()
que.append([0,N,0])
tmp = 21e8
cnt = 0
cnt_lst = [[21e8, 1] for _ in range(100001)]
cnt_lst[N] = [0,1]
while que :
    level, now, prev = que.popleft()
    if now < 0 or now > 100000 :
        continue
    
    if level > tmp :
        break

    if now == M :
        if tmp > level :
            tmp = level
            cnt = cnt_lst[prev][1]
        elif tmp == level :
            cnt += cnt_lst[prev][1]

    else :
        if cnt_lst[now][0] == 21e8 :
            cnt_lst[now] = [level, cnt_lst[prev][1]]
        elif cnt_lst[now][0] == level :
            cnt_lst[now][1] *= cnt_lst[prev][1]
        else :
            continue

    if 0 <= now <= 100000 :
        que.append([level+1, now-1, now]) 
        que.append([level+1, now+1, now]) 
        que.append([level+1, 2*now, now])

print(tmp)
print(cnt)