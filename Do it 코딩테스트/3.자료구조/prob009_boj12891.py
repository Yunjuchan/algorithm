import sys
input = sys.stdin.readline
S, P = map(int, input().split())
DNA = input()
ACGT = list(map(int, input().split()))
cnt = 0
now = [0] * 4
for i in range(P) :
    if DNA[i] == 'A' :
        now[0] += 1
    elif DNA[i] == 'C' :
        now[1] += 1
    elif DNA[i] == 'G' :
        now[2] += 1
    elif DNA[i] == 'T' :
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
    if lst[0] >= ACGT[0] and lst[1] >= ACGT[1] and lst[2] >= ACGT[2] and lst[3] >= ACGT[3]:
        return 1
    return 0

for i in range(S-P+1) :
    if D(now) == 1 :
        cnt += 1
    if i != (S-P) :   
        minus(DNA[i])
        add(DNA[i+P])
    else : 
        break 
print(cnt)
