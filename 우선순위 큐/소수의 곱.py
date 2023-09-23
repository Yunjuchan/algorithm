from heapq import heappush, heappop
K, N = map(int, input().split())
sosu = list(map(int, input().split()))
que = []
Max = max(sosu)
for i in range(K) :
    heappush(que, [sosu[i], i])
    
cnt = 0
length = K
while True :
    x = heappop(que)
    cnt += 1
    last = x[0]
    if cnt == N :
        print(x[0])
        break
    for i in range(x[1], K) :
        if length >= (N) :
            if x[0]*sosu[i] > Max :
                continue

        length += 1
        heappush(que, [x[0]*sosu[i], i])
        if Max < x[0] * sosu[i] :
            Max = x[0] * sosu[i]