from collections import deque
def delete(flag) :
    if flag == 1 :
        que.popleft()
    else :
        que.pop()
        
def out(flag) :
    tmp = []
    if flag == 0 :
        while que :
            tmp.append(que.pop())
    else :
        while que :
            tmp.append(que.popleft())
    print('[', end='')
    print(*tmp, sep=',', end='')
    print(']')

T = int(input())
for _ in range(T) :
    flag = 1
    flag2 = 0
    command = input()
    N = int(input())
    lst = input()
    if N == 0 :
        if command.count('D') != 0 :
            print('error')
            continue
        else :
            print(lst)
            continue

    que = deque(map(int, lst[1:-1].split(',')))

    for c in command :
        if c == 'D' :
            if not que :
                print('error')
                flag2 = 1
                break
            delete(flag)
        else :
            flag = (flag + 1) % 2
    if flag2 == 1 :
        continue
    out(flag)