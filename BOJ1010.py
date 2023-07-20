N, M = map(int, input().split())
def bridge(n, m) :
    total = 0
    if n == 1:
        return m
    for i in range(1, m-n+2) :
        total += bridge(n-1, m-i)
    return total
        
bridge(N, M)

# 이거를 속도를 빠르게 어떻게 할 수 있을까