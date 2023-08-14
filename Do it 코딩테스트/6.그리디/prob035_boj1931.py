import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N) :
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x : x[0])
lst.sort(key=lambda x : x[1])
cnt = 0
# tmp = [0, 0]
end = 0
for i in range(N) :
    if lst[i][0] >= end :
        end = lst[i][1]
        cnt += 1
    # elif lst[i][1] < tmp[1] :
    #     tmp = lst[i]
print(cnt)