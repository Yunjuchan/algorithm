import sys
input = sys.stdin.readline
tc = 1
while True :
    N = int(input())
    children = []
    message = []
    flag = 0
    if N == 0 :
        break
    for i in range(N) :
        children.append(input().split())
    print(f'Group {tc}')
    for i in range(N) :
        for j in range(N) :
            if children[i][j] == 'N' :
                flag = 1
                print(f'{children[(i-j) % N][0]} was nasty about {children[i][0]}')
    if flag == 0 :
        print('Nobody was nasty')
    print()
    tc += 1