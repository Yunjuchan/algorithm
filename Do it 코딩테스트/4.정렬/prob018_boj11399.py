N = int(input())
lst = list(map(int, input().split()))
bucket = [0] * 1001
sorted_lst = [0] * N
delay = 0
for i in range(N) :
    bucket[lst[i]] += 1

for i in range(1, 1001) :
    bucket[i] += bucket[i-1]

for i in range(N) :
    bucket[lst[i]] -= 1
    sorted_lst[bucket[lst[i]]] = lst[i]

for i in range(1, N) :
    sorted_lst[i] += sorted_lst[i-1]

for i in range(N) :
    delay += sorted_lst[i]
 
print(delay)