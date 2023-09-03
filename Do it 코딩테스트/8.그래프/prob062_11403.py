N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
    for j in range(N) :
        for k in range(N) :
            if adj[j][i] == adj[i][k] == 1 :
                adj[j][k] = 1
for a in adj :
    print(*a)