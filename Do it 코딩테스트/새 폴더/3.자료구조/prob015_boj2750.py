import sys
sys.stdin.readline
N = int(input())
lst = []
for i in range(N) :
    lst.append(int(input()))

for i in range(N) : 
    for j in range(N-i-1) :
        if lst[j] > lst[j+1] :
            lst[j], lst[j+1] = lst[j+1], lst[j]
for x in lst :
    print(x)