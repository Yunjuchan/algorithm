A, B, C = map(int, input().split())
result = 0
def abc(a, n) :
    if n == 1 :
        return a % C
    else :
        tmp = abc(a, n//2)
        if n % 2 == 1 :
            return (tmp*tmp*a) % C
        else :
            return tmp**2 % C

ret = abc(A, B)
print(ret)


