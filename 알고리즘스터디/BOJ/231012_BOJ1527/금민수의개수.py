A, B = map(int, input().split())
L = ['4', '7']
cnt = 0
def dfs(x) :
    global cnt
    if A <= int(x) <= B :
        cnt += 1
    if int(x) > B :
        return
    for i in L :
        dfs(x+i)
dfs('0')
print(cnt)