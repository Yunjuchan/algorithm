N, D = map(int, input().split())
A = [i for i in range(D+1)]
road = []
for _ in range(N) :
    road.append(list(map(int, input().split())))
road.sort(key=lambda x : (x[0], x[2]-x[1]+x[0]))
for i in range(N) :
    if road[i][1] > D :
        continue
    if A[road[i][0]] + road[i][2] < A[road[i][1]] :
        A[road[i][1]] = A[road[i][0]] + road[i][2]
        for j in range(road[i][1], D) :
            if A[j+1] <= A[j] + 1 :
                break
            A[j+1] = A[j] + 1
print(A[D])
