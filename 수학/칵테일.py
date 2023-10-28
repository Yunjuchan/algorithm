def gcd(a, b) :
    if a < b :
        a, b = b, a
    while b :
        tmp = a % b
        a = b
        b = tmp
    return a

N = int(input())
arr = [0] * N
for _ in range(N-1) :
    a, b, p, q = map(int, input().split())
    g = (gcd(p, q))
    p //= g
    q //= g
    if arr[a] == 0 :
        for i in range(N) :
            arr[i]
    elif arr[b] == 0 :
        pass
    elif arr[a] % p and arr[b] % q :
        pass
    elif arr[a] % p :
        pass
    else :
        pass
