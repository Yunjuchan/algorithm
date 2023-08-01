'''
교감선생님께 귀걸이를 뺏겼는데 
교감선생님이 귀걸이 하나를 잃어버림

귀걸이는 여학생의 번호와 A 또는 B가 같이 적혀있다.
귀걸이를 받지 못한 여학생은?

'''
import sys
input = sys.stdin.readline
cnt = 1
while True :
    name_list = []
    status = {}
    N = int(input())    # 귀걸이를 뺏긴 여학생의 수
    if N == 0 :
        break
    for i in range(N) :
        name_list.append(input())
    for i in range(2*N-1) :
        x = input().split()
        status[x[0]] = status.get(x[0],[]) + [x[1]]
    for k, v in status.items() :
        k = int(k)
        if len(v) == 1 :
            print(f'{cnt} {name_list[k-1]}', end='')
    cnt += 1

## 왜 한줄이 띄어져서 나오는지 의문!
    
    