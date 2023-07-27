import math
Prime = [1]*1001
Prime[0] = Prime[1] = 0
for i in range(2, 1001) :
    for j in range(2, int(math.sqrt(i))+1) :
        if i % j == 0 :
            Prime[i] = 0
            break

N = int(input())
num_list = list(map(int, input().split()))
cnt = 0
for num in num_list :
    if Prime[num] == 1 :
        cnt += 1
print(cnt)