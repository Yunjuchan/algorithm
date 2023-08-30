import sys
input = sys.stdin.readline
# 지민이의 인덱스를 0으로 두고 풀이
def union(a, b) :               
    fa, fb = map(find, [a, b])
    if fa == fb :
        return 1
    top[fb] = fa
    return 0
def find(x) :
    if top[x] == -1 :
        return x
    ret = find(top[x])
    top[x] = ret
    return ret
N, M = map(int, input().split())
top = [-1] * (N+1)
X, *lst = map(int, input().split())
party_list = []
for i in range(X) :
    union(0, lst[i])
for _ in range(M) :
    Y, *lst2 = map(int, input().split())
    party_list.append(lst2[:])

while True :
    flag = 0
    for lst2 in party_list :   
        for j in lst2 :
            if find(j) == 0 :
                flag = 1
                for j in lst2 :
                    union(0, j)
                party_list.remove(lst2)
                break
    if flag == 0 :
        break
print(len(party_list))

