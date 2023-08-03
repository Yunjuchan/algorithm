import sys
input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]
bucket = [0] * 10001
for i in range(N) :
    bucket[lst[i]] += 1
for i in range(1, 10001) :
    if bucket[i] != 0 :
        for j in range(bucket[i]) :
            print(i)



