import sys
input = sys.stdin.readline
N = int(input())
switch = [0] + list(map(int, input().split()))
def boy(x) :
    for i in range(1, N//x+1) :
        switch[x*i] = (switch[x*i] + 1) % 2

def girl(x) :
    i = 1
    while True :
        i += 1
        if x-i == 0 or x+i == N :
            i -= 1
            break
        if switch[x-i] == switch[x+i] :
            continue
        else :
            x -= 1
            break
    while i != 0 :
        switch[x-i] = (switch[x-i] + 1) % 2
        switch[x+i] = (switch[x+i] + 1) % 2
        i -= 1
    switch[x] = (switch[x] + 1) % 2

M = int(input())
for i in range(M) :
    s, n = map(int, input().split())
    if s == 1 :
        boy(n)
    else :
        girl(n)
print(*switch[1:])
