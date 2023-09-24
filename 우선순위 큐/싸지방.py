from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
A = []
result = [0] * 100001
k = 1
computer = [[0,1]]
empty = []
for _ in range(N) :
    heappush(A, list(map(int, input().split())))
while A :
    s, e = heappop(A)
    if empty :
        if empty[0] >= computer[0][0] or (s < computer[0][0]) :
            n = heappop(empty)
            heappush(computer, [e, n])
            result[n] += 1
            continue
    end, n= heappop(computer)
    if s < end :
        k += 1
        heappush(computer, [e, k])
        result[k] = 1
        heappush(computer, [end, n])
    else :
        heappush(empty, n)
        while computer :
            end, n = heappop(computer)
            if s < end :
                heappush(computer, [end, n])
                n2 = heappop(empty)
                heappush(computer, [e, n2])
                result[n2] += 1
                break
            heappush(empty, n)
        else :
            n2 = heappop(empty)
            heappush(computer, [e, n2])
            result[n2] += 1

            
print(k)
for i in range(1, 100001) :
    if result[i] == 0 :
        break
    print(result[i], end=' ')

