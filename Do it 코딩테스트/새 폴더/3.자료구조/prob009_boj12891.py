import sys
input = sys.stdin.readline
S, P = map(int, input().split())
DNA = input()
A,C,G,T = map(int, input().split())
bucket = set()
now = [0] * 4
for i in range(P) :
    if i == 'A' :
        now[0] += 1
    elif i == 'C' :
        now[1] += 1
    elif i == 'G' :
        now[2] += 1
    elif i == 'T' :
        now[3] += 1

def add(char) :
    if char == 'A' :
        now[0] += 1
    elif char == 'C' :
        now[1] += 1
    elif char == 'G' :
        now[2] += 1
    elif char == 'T' :
        now[3] += 1

def minus(char) :
    if char == 'A' :
        now[0] -= 1
    elif char == 'C' :
        now[1] -= 1
    elif char == 'G' :
        now[2] -= 1
    elif char == 'T' :
        now[3] -= 1

def D(lst) :
    if lst[0] >= A and lst[1] >= C and lst[2] >= G and lst[3] >= T:
        return 1
    return 0

for i in range(S-P+1) :

    if D(now) == 1 :
        bucket.add(DNA[:])
    DNA[i]
print(len(bucket))
