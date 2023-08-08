import sys
input = sys.stdin.readline

def distance(eswn1, n1, eswn2, n2) :
    if eswn1 == 1:
        if eswn2 == 1 :
            distance = max(n1-n2, n2-n1)
        elif eswn2 == 3 :
            distance = n1 + n2
        elif eswn2 == 4 :
            distance = (x-n1) + n2
        else :
            distance = y + min(n1+n2, 2*x-n1-n2)
    elif eswn1 == 2 :
        if eswn2 == 2 :
            distance = max(n1-n2, n2-n1)
        elif eswn2 == 3 :
            distance = n1 + (y-n2)
        elif eswn2 == 4 :
            distance = (x-n1) + (y-n2)
        else :
            distance = y + min(n1+n2, 2*x-n1-n2)
    elif eswn1 == 3 :
        if eswn2 == 3 :
            distance = max(n1-n2, n2-n1)
        elif eswn2 == 1 :
            distance = n1 + n2
        elif eswn2 == 2 :
            distance = n2 + (y-n1)
        else :
            distance = x + min(n1+n2, 2*y-n1-n2)
    else :
        if eswn2 == 4 :
            distance = max(n1-n2, n2-n1)
        elif eswn2 == 1 :
            distance = (x-n2) + n1
        elif eswn2 == 2 :
            distance = (x-n2) + (y-n1)
        else :
            distance = x + min(n1+n2, 2*y-n1-n2)
    return distance


x, y = map(int, input().split())
N = int(input())
total = 0
X = []
for i in range(N) :
    X.append(list(map(int, input().split())))
dong_ewsn, dong_n = map(int, input().split())
for i in range(N) :
    total += distance(dong_ewsn, dong_n, *X[i])
print(total)
