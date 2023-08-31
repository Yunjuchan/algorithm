from collections import deque as q
N = int(input())
adj = [[] for _ in range(N+1)] 
lst = [0] * (N+1)
time_list = [0]*(N+1)
for i in range(1, N+1) :
    time, *pre, stop = map(int, input().split())
    time_list[i] = time
    lst[i] = len(pre)
    for x in pre :
        adj[x].append(i)
new_time = time_list[:]

q = q()
for i in range(1, N+1) :
    if lst[i] == 0 :
        q.append(i)

while q :
    x = q.popleft()
    for i in adj[x] :
        lst[i] -= 1
        if time_list[i] + new_time[x] > new_time[i] :
            new_time[i] = time_list[i] + new_time[x] 
        if lst[i] == 0 :
            q.append(i)
for x in new_time[1:] :
    print(x)
