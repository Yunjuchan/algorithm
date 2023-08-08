import sys 
input = sys.stdin.readline
N = int(input())
lst = []
move_list = []
idx = 1
for i in range(N) :
    x = int(input())
    while idx <= x :
        lst.append(idx)
        move_list.append('+') 
        idx += 1

    while lst[-1] == x :
        if lst[-1] == x :
            lst.pop()
            move_list.append('-')
            break
    else :
        print('NO')
        break
else :
    for m in move_list :
        print(m)