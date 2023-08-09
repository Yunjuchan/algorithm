def max_num(level):
    if level == len(str(N)):
        if int(''.join(map(str,path))) <= N:
            new_lst.append(''.join(map(str,path)))
        return
    if path != [] :
        new_lst.append(''.join(map(str,path)))
    for i in range(K):
        path[len(str(N))-level-1] = k[i]
        max_num(level+1)
        path[len(str(N))-level-1] = 0



N,K = map(int,input().split())
new_lst = []
st_N = str(N)
k = list(map(int,input().split()))
path = [0] * len(str(N))
max_num(0)
new_lst = list(map(int, new_lst))
print(max(new_lst))