N = int(input())
lst = []
bucket = [0] * 101 
idx = 100
dasom = int(input())
cnt = 0
for i in range(N-1) :
    x = int(input())
    lst.append(x)
for i in lst :
    bucket[i] += 1
while dasom <= idx and idx > 0:
    if bucket[idx] != 0 :
        bucket[idx] -= 1
        bucket[idx-1] += 1
        dasom += 1
        cnt += 1
    else :
        idx -= 1
print(cnt)

