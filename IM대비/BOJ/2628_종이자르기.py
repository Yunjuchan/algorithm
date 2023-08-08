import sys
input = sys.stdin.readline
c, r = map(int, input().split())
N = int(input())
r_cut = [0, r]
c_cut = [0, c]
for i in range(N) :
    how, n = map(int, input().split())
    if how == 0 :
        r_cut.append(n)
    else :
        c_cut.append(n)
r_cut.sort()
c_cut.sort()
r_max = c_max = 0
for i in range(1,len(r_cut)) :
    if r_cut[i] - r_cut[i-1]  > r_max :
        r_max = r_cut[i] - r_cut[i-1]

for i in range(1,len(c_cut)) :
    if c_cut[i] - c_cut[i-1]  > c_max :
        c_max = c_cut[i] - c_cut[i-1]
print(c_max * r_max)