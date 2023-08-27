N, M = map(int, input().split())
dic = dict()
cnt = 0
lst = []
for _ in range(N) :
    dic[input()] = 1

for _ in range(M) :
    x = input()
    dic[x] = dic.get(x,0) + 1
    if dic[x] == 2 :
        cnt += 1
    
print(cnt)
for k, v in dic.items() :
    if v == 2 :
        lst.append(k)
lst.sort()
for i in lst :
    print(i)
