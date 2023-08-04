# 숫자는 최대 1억
import sys
N = int(input())
# 내 풀이 메모리 초과
# prime = [True] * (10 ** 8 + 1)
# prime[0] = prime[1] = False
# for i in range(2, 10 ** 4 + 1) :
#     for j in range(i*i, (10 ** 4 + 1) // i) :
#         prime[i*j] = False

# def DFS(x) :
#     if x == 0 :
#         return 1
#     if prime[x] :
#         if not DFS(x // 10) :
#             return 0
#     else : return 0
    
#     return 1

def is_prime(x) :
    for i in range(2, int(x**(1/2))+1) :
        if x % i == 0 :
           return 0
        else :
            continue
    return 1

def DFS(x) :
    if len(str(x)) == N and is_prime(x):
        print(x)
    else :
        if is_prime(x) : 
            for i in range(1, 10, 2) :
                DFS(x*10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)