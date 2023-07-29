import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for n in range(N) :
    x = input()
    st = set([x[0]])
    tmp = 0
    i = 0
    if len(x) == 1 :
        cnt += 1
        continue
    while i < len(x) - 1 :
        if x[i] != x[i+1] :
            st.add(x[i+1])
            tmp += 1
        i += 1
    if len(st) - 1 == tmp :
        cnt += 1
print(cnt)