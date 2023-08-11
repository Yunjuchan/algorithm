def RCS(a, b):
    if lst[a] == lst[b]:
        return a
    elif lst[a] - lst[b] == 1 or lst[a] - lst[b] == -2:
        return a
    elif lst[a] - lst[b] == -1 or lst[a] - lst[b] == 2:
        return b
 
def Team(N, lst):
    temp = [[], []]
    mid = (N+1) // 2    # len을 이렇게 쓰면 밑에 따로 조건 안써두 될듯!

    temp[0] = lst[:mid]
    temp[1] = lst[mid:]
    for i in range(2):
        if len(temp[i])>2:
            temp[i] = Team(mid, temp[i])
    for i in range(2):
        if len(temp[i]) == 2:
            temp[i] = RCS(temp[i][0], temp[i][1])
        elif len(temp[i]) == 1:
            temp[i] = temp[i][0]
    return temp
 
T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst2 = list(range(N))
 
    lst2 = Team(N, lst2)
    ans = RCS(lst2[0], lst2[1])
 
    print(f'#{tc} {ans+1}')