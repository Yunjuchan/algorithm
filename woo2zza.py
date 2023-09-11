A, B = map(int, input().split())

def count(num) :
    i = 0
    lst = [0] * 60
    while num :
        tmp = num // 2**i
        lst[i] = ((tmp + 1) // 2) * 2 ** i
        if lst[i] == 0 :
            break
        if tmp % 2 != 0 :
            lst[i] -= (tmp+1)*2**(i) - 1 - num
        i += 1
    return sum(lst)
print(count(B) - count(A-1))
